# perlipc
Perl interprocess communication (signals, fifos, pipes, safe subprocesses, sockets, and semaphores)
https://perldoc.perl.org/index.html

## Signals
%SIG contains names or user-installed signal handler.

Signals come from:
1. keyboard sequence, e.g. Ctrl-C (SIGINT), Ctrl-Z (SIGTSTP).
2. kernel, e.g. when child process exiting, current process running out of stack, hitting process size limit.

e.g. trap an interrupt signal and set up a handler:
```
    sub onSIGINT {
        my $signame = shift;
        die "Somebody sent me a SIG$signame!";
    }
    $SIG{INT} = __PACKAGE . "::onSIGINT";
```

List signals from current systems:
$ kill -l
1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL       5) SIGTRAP
6) SIGABRT      7) SIGBUS       8) SIGFPE       9) SIGKILL     10) SIGUSR1
...

Sending **a signal to a negative process ID** means that you send the signal to the entire Unix process group.
This code sends a hang-up signal to all processes in the current process group, and also sets $SIG{HUP} to "IGNORE"
so it doesn't kill itself:
```
    # block scope for local
    {
        local $SIG{HUP} = "IGNORE";
        kill HUP => -$$;
        # snazzy writing of: kill("HUP", -$$)
    }
```

Another interesting signal to send is **signal number zero**.
This doesn't actually affect a child process, but instead checks whether it's alive or has changed its UIDs.
```
    unless (kill 0 => $kid_pid) {
        warn "something wicked happened to $kid_pid";
    }
```

Signal number zero may fail because you lack permission to send the signal when directed at a process
whose real or saved UID is not identical to the real or effective UID of the sending process,
even though the process is alive. You may be able to determine the cause of failure using $! or %! .
```
    unless (kill(0 => $pid) || $!{EPERM}) {
        warn "$pid looks dead";
}
```

Employ anonymous functions for simple signal handlers:
```
    $SIG{INT} = sub { die "\nOutta here!\n"  };
```

SIGCHLD handlers require some special care. If a second child dies while in the signal handler caused by the first death,
we won't get another signal. So must loop here else we will leave the unreaped child as a zombie.
```
    use POSIX ":sys_wait_h";
    $SIG{CHLD} = sub {
        while ((my $child = waitpid(-1, WNOHANG)) > 0) {
            $Kid_Status{$child} = $?;
        }
    };
    # do something that forks...
```
**waitpid**>>>
waitpid PID,FLAGS
Waits for a particular child process to terminate and
returns __the pid of the deceased process__,
or __-1__ if there is no such child process,
or __0__ (on some systems) indicates that there are processes still running. The status is returned in $? .
FLAGS:
WNOHANG - This flag specifies that waitpid should return immediately instead of waiting,if there is no child process ready to be noticed.
<<<

Be careful not to have child process call your handler...
TODO: Discover more for parent and child signal handling...

Signal handling is also used for timeouts in Unix.
```
    my $ALARM_EXCEPTION = "alarm clock restart";
    eval {
        local $SIG{ALRM} = sub { die $ALARM_EXCEPTION };
        alarm 10;
        flock(FH, 2)    # blocking write lock
                        || die "cannot flock: $!";
        alarm 0;
    };
    if ($@ && $@ !~ quotemeta($ALARM_EXCEPTION)) { die }
```
**alarm**>>>
alarm SECONDS
Arranges to have a SIGALRM delivered to this process after the specified number of wallclock seconds has elapsed.
If SECONDS is not specified, the value stored in $\_ is used. (On some machines, unfortunately, the elapsed time
may be up to one second less or more than you specified because of how seconds are counted, and process scheduling
may delay the delivery of the signal even further.)

Only one timer may be counting at once. Each call disables the previous timer, and an argument of 0 may be supplied
to cancel the previous timer without starting a new one. The returned value is the amount of time remaining on the previous timer.
```
    eval {
        local $SIG{ALRM} = sub { die "alarm\n" }; # NB: \n required
        alarm $timeout;
        my $nread = sysread $socket, $buffer, $size;
        alarm 0;
    };
    if ($@) {
        if ($@ eq "alarm\n") { #timed out }
        die $@; # propagate unexpected errors
    }
```
<<<

### Handling the SIGHUP Signal in Daemons
A process that usually starts when the system boots and shuts down when the system is shut down is called a daemon (Disk And Execution MONitor).
If a daemon process has a configuration file which is modified after the process has been started,
there should be a way to tell that process to reread its configuration file without stopping the process.
Many daemons provide this mechanism using a SIGHUP signal handler. When you want to tell the daemon to
reread the file, simply send it the SIGHUP signal.
```
  #!/usr/bin/perl
  use strict;
  use warnings;

  use POSIX ();
  use FindBin ();
  use File::Basename ();
  use File::Spec::Functions qw(catfile);

  $| = 1;

  # make the daemon cross-platform, so exec always calls the script
  # itself with the right path, no matter how the script was invoked.
  my $script = File::Basename::basename($0);
  my $SELF  = catfile($FindBin::Bin, $script);

  # POSIX unmasks the sigprocmask properly
  $SIG{HUP} = sub {
      print "got SIGHUP\n";
      exec($SELF, @ARGV)        || die "$0: couldn't restart: $!";
  };

  code();

  sub code {
      print "PID: $$\n";
      print "ARGV: @ARGV\n";
      my $count = 0;
      while (1) {
          sleep 2;
          print ++$count, "\n";
      }
  }
```
**exec**>>>
exec PROGRAM LIST
The exec function executes a system command and never returns.
<<<
e.g.
$ perl /home/vagrant/test.pl
PID: 31082
ARGV:
1
2
got SIGHUP
going to exec /home/vagrant/test.pl
PID: 31082
ARGV:
1
2
3
Killed
$ kill -1 31082
$ kill -1 31082 # no reaction as it's executed from **exec**
$ kill -9 31082


### Deferred Signals (Safe Signals)
...

e.g.
```
    use POSIX qw(SIGALRM);
    POSIX::sigaction(SIGALRM,
                     POSIX::SigAction->new(sub { die "alarm" }))
             || die "Error setting SIGALRM handler: $!\n";

```


### Named Pipes
A named pipe (often referred to as a FIFO) is an old Unix IPC mechanism for processes communicating on the same machine.
It works just like regular anonymous pipes, except that the processes rendezvous using a filename and need not be related.

To create a named pipe:
```
    use POSIX qw(mkfifo);
    mkfifo($path, 0700)     ||  die "mkfifo $path failed: $!";
```

A fifo is convenient when you want to connect a process to an unrelated one.
When you open a fifo, the program will block until there's something on the other end.
For example, let's say you'd like to have your .signature file be a named pipe that has a Perl program on the other end.
Now every time any program (like a mailer, news reader, finger program, etc.) tries to read from that file,
the reading program will read the new signature from your program.
```
    chdir();    # go home
    my $FIFO = ".signature";
    while (1) {
        unless (-p $FIFO) {
            unlink $FIFO;   # discard any failure, will catch later
            require POSIX;  # delayed loading of heavy module
            POSIX::mkfifo($FIFO, 0700)
                                || die "can't mkfifo $FIFO: $!";
        }
        # next line blocks till there's a reader
        open (FIFO, "> $FIFO")  || die "can't open $FIFO: $!";
        print FIFO "John Smith (smith\@host.org)\n", `fortune -s`;
        close(FIFO)             || die "can't close $FIFO: $!";
        sleep 2;                # to avoid dup signals
    }
```


### Using open() for IPC
Perl's basic open() statement can also be used for unidirectional interprocess communication by
either appending or prepending a pipe symbol to the second argument to open().


### Filehandles
Both the main process and any child processes it forks share the same STDIN, STDOUT, and STDERR filehandles.
If both processes try to access them at once, strange things can happen. You may also want to close or reopen the filehandles for the child.
You can get around this by opening your pipe with open(), but on some systems this means that the child process cannot outlive the parent.


### Complete Dissociation of Child from Parent
In some cases (starting server processes, for instance) you'll want to completely dissociate the child process from the parent.
This is often called **daemonization**.
A well-behaved daemon will also chdir() to the root directory so it doesn't prevent
unmounting the filesystem containing the directory from which it was launched,
and redirect its standard file descriptors from and to /dev/null so that
random output doesn't wind up on the user's terminal.
```
 use POSIX "setsid";
 sub daemonize {
     chdir("/")                  || die "can't chdir to /: $!";
     open(STDIN,  "< /dev/null") || die "can't read /dev/null: $!";
     open(STDOUT, "> /dev/null") || die "can't write to /dev/null: $!";
     defined(my $pid = fork())   || die "can't fork: $!";
     exit if $pid;               # non-zero now means I am the parent
     (setsid() != -1)            || die "Can't start a new session: $!";
     open(STDERR, ">&STDOUT")    || die "can't dup stdout: $!";
 }

```


### Safe Pipe Opens
...

### Avoiding Pipe Deadlocks
...

### Bidirectional Communication with Another Process
```
    use FileHandle;
    use IPC::Open2;
    $pid = open2(*Reader, *Writer, "cat -un");
    print Writer "stuff\n";
    $got = <Reader>;
```
...

### Bidirectional Communication with Yourself
If you want, you may make low-level pipe() and fork() syscalls to stitch this together by hand.
This example only talks to itself, but you could reopen the appropriate handles to STDIN and STDOUT and call other processes.
(The following example lacks proper error checking.)
```
    #!/usr/bin/perl -w
    # pipe1 - bidirectional communication using two pipe pairs
    #         designed for the socketpair-challenged
    use IO::Handle;             # thousands of lines just for autoflush :-(

    # child read from, parent write to
    pipe(PARENT_RDR, CHILD_WTR);  # XXX: check failure?
    # parent read from, child write to
    pipe(CHILD_RDR,  PARENT_WTR); # XXX: check failure?
    CHILD_WTR->autoflush(1);
    PARENT_WTR->autoflush(1);

    if ($pid = fork()) {
       # Parent
        close PARENT_RDR;
        close PARENT_WTR;
        print CHILD_WTR "Parent Pid $$ is sending this\n";
        chomp($line = <CHILD_RDR>);
        print "Parent Pid $$ just read this: '$line'\n";
        close CHILD_RDR;
        close CHILD_WTR;
        waitpid($pid, 0);
    } else {
       # Child
        die "cannot fork: $!" unless defined $pid;
        close CHILD_RDR;
        close CHILD_WTR;
        chomp($line = <PARENT_RDR>);
        print "Child Pid $$ just read this: '$line'\n";
        print PARENT_WTR "Child Pid $$ is sending this\n";
        close PARENT_RDR;
        close PARENT_WTR;
        exit(0);
    }
```
**pipe**>>>
pipe READHANDLE,WRITEHANDLE
Opens a pair of connected pipes like the corresponding system call.
Returns true on success.
<<<

But you don't actually have to make two pipe calls.
If you have the socketpair() system call, it will do this all for you.
```
    #!/usr/bin/perl -w
    # pipe2 - bidirectional communication using socketpair
    #   "the best ones always go both ways"
    use Socket;
    use IO::Handle;  # thousands of lines just for autoflush :-(

    # We say AF_UNIX because although *_LOCAL is the
    # POSIX 1003.1g form of the constant, many machines
    # still don't have it.
    socketpair(CHILD, PARENT, AF_UNIX, SOCK_STREAM, PF_UNSPEC)
                                ||  die "socketpair: $!";
    CHILD->autoflush(1);
    PARENT->autoflush(1);

    if ($pid = fork()) {
        # Parent
        close PARENT;
        print CHILD "Parent Pid $$ is sending this\n";
        chomp($line = <CHILD>);
        print "Parent Pid $$ just read this: '$line'\n";
        close CHILD;
        waitpid($pid, 0);
        print "Parent exiting...\n";
    } else {
        # Child
        die "cannot fork: $!" unless defined $pid;
        close CHILD;
        chomp($line = <PARENT>);
        print "Child Pid $$ just read this: '$line'\n";
        print PARENT "Child Pid $$ is sending this\n";
        close PARENT;
        exit(0);
    }
```


### Sockets: Client/Server Communication

#### Internet Line Terminators
The Internet line terminator is "\015\012". Under ASCII variants of Unix, that could usually be written as "\r\n".

#### Internet TCP Clients and Servers
A sample TCP client:
```
    #!/usr/bin/perl -w
    use strict;

    use Socket;

    my ($remote, $port, $iaddr, $paddr, $proto, $line);
    $remote  = shift || "localhost";
    $port    = shift || 2345;  # random port
    if ($port =~ /\D/) { $port = getservbyname($port, "tcp") }
    die "No port" unless $port;
    $iaddr   = inet_aton($remote)       || die "no host: $remote";
    $paddr   = sockaddr_in($port, $iaddr);
    $proto   = getprotobyname("tcp");

    socket(SOCK, PF_INET, SOCK_STREAM, $proto)  || die "socket: $!";
    connect(SOCK, $paddr)               || die "connect: $!";
    while ($line = <SOCK>) {
        print $line;
    }

    close (SOCK)                        || die "close: $!";
    exit(0);
```

A sample TCP server:
```
    #!/usr/bin/perl -Tw
    use strict;

    BEGIN { $ENV{PATH} = "/usr/bin:/bin" }
    use Socket;
    use Carp;

    my $EOL = "\015\012";
    sub logmsg { print "$0 $$: @_ at ", scalar localtime(), "\n" }
    my $port  = shift || 2345;
    die "invalid port" unless $port =~ /^ \d+ $/x;
    my $proto = getprotobyname("tcp");

    socket(Server, PF_INET, SOCK_STREAM, $proto)   || die "socket: $!";
    setsockopt(Server, SOL_SOCKET, SO_REUSEADDR, pack("l", 1))
                                                   || die "setsockopt: $!";
    bind(Server, sockaddr_in($port, INADDR_ANY))   || die "bind: $!";
    listen(Server, SOMAXCONN)                      || die "listen: $!";
    logmsg "server started on port $port";

    my $paddr;
    for ( ; $paddr = accept(Client, Server); close Client) {
        my($port, $iaddr) = sockaddr_in($paddr);
        my $name = gethostbyaddr($iaddr, AF_INET);
        logmsg "connection from $name [",
                inet_ntoa($iaddr), "]
                             at port $port";
        print Client "Hello there, $name, it's now ",
                        scalar localtime(), $EOL;
    }
```
**pack**>>>
pack TEMPLATE,LIST
Takes a LIST of values and converts it into a string using the rules given by the TEMPLATE.
The resulting string is the concatenation of the converted values. Typically,
each converted value looks like its machine-level representation.
For example, on 32-bit machines an integer may be represented by a sequence of 4 bytes,
which will in Perl be presented as a string that's 4 characters long.
TEMPLATE:
l - A signed long (32-bit) value.
W - An unsigned char value (can be greater than 255).
...
e.g.
    print pack("W*", 65..90);
    >>> "A..Z"
<<<

Here's a multitasking version. It's multitasked in that like most typical servers,
it spawns (fork()s) a slave server to handle the client request so that the master server can quickly go back to service a new client.
```
    #!/usr/bin/perl -Tw
    use strict;
    BEGIN { $ENV{PATH} = "/usr/bin:/bin" }
    use Socket;
    use Carp;

    my $EOL = "\015\012";
    sub spawn;  # forward declaration
    sub logmsg { print "$0 $$: @_ at ", scalar localtime(), "\n" }
    my $port  = shift || 2345;
    die "invalid port" unless $port =~ /^ \d+ $/x;
    my $proto = getprotobyname("tcp");

    socket(Server, PF_INET, SOCK_STREAM, $proto)   || die "socket: $!";
    setsockopt(Server, SOL_SOCKET, SO_REUSEADDR, pack("l", 1))
                                                   || die "setsockopt: $!";
    bind(Server, sockaddr_in($port, INADDR_ANY))   || die "bind: $!";
    listen(Server, SOMAXCONN)                      || die "listen: $!";
    logmsg "server started on port $port";

    my $waitedpid = 0;
    my $paddr;
    use POSIX ":sys_wait_h";
    use Errno;
    sub REAPER {
        local $!;   # don't let waitpid() overwrite current error
        while ((my $pid = waitpid(-1, WNOHANG)) > 0 && WIFEXITED($?)) {
            logmsg "reaped $waitedpid" . ($? ? " with exit $?" : "");
        }
        $SIG{CHLD} = \&REAPER;  # loathe SysV
    }
    $SIG{CHLD} = \&REAPER;

    while (1) {
        $paddr = accept(Client, Server) || do {
            # try again if accept() returned because got a signal
            next if $!{EINTR};
            die "accept: $!";
        };
        my ($port, $iaddr) = sockaddr_in($paddr);
        my $name = gethostbyaddr($iaddr, AF_INET);
        logmsg "connection from $name [",
               inet_ntoa($iaddr),
               "] at port $port";
        spawn sub {
            $| = 1;
            print "Hello there, $name, it's now ",
                  scalar localtime(),
                  $EOL;
            exec "/usr/games/fortune"       # XXX: "wrong" line terminators
                or confess "can't exec fortune: $!";
        };
        close Client;
    }

    sub spawn {
        my $coderef = shift;
        unless (@_ == 0 && $coderef && ref($coderef) eq "CODE") {
            confess "usage: spawn CODEREF";
        }
        my $pid;
        unless (defined($pid = fork())) {
            logmsg "cannot fork: $!";
            return;
        }
        elsif ($pid) {
            logmsg "begat $pid";
            return; # I'm the parent
        }
        # else I'm the child -- go spawn
        open(STDIN,  "<&Client")    || die "can't dup client to stdin";
        open(STDOUT, ">&Client")    || die "can't dup client to stdout";
        ## open(STDERR, ">&STDOUT") || die "can't dup stdout to stderr";
        exit($coderef->());
    }
```

#### Unix-Domain TCP Clients and Servers
Unix-domain sockets are local to the current host, and are often used internally to implement pipes.
Unlike Internet domain sockets, Unix domain sockets can show up in the file system with an ls(1) listing.

A sample Unix-Domain client:
```
    #!/usr/bin/perl -w
    use strict;

    use Socket;

    my ($rendezvous, $line);
    $rendezvous = shift || "catsock";
    socket(SOCK, PF_UNIX, SOCK_STREAM, 0)     || die "socket: $!";
    connect(SOCK, sockaddr_un($rendezvous))   || die "connect: $!";
    while (defined($line = <SOCK>)) {
        print $line;
    }
    exit(0);
```

A sample Unix-Domain Server:
```
    #!/usr/bin/perl -Tw
    use strict;

    use Socket;
    use Carp;
    BEGIN { $ENV{PATH} = "/usr/bin:/bin" }

    sub spawn;  # forward declaration
    sub logmsg { print "$0 $$: @_ at ", scalar localtime(), "\n" }
    my $NAME = "catsock";
    my $uaddr = sockaddr_un($NAME);
    my $proto = getprotobyname("tcp");

    socket(Server, PF_UNIX, SOCK_STREAM, 0) || die "socket: $!";
    unlink($NAME);
    bind  (Server, $uaddr)                  || die "bind: $!";
    listen(Server, SOMAXCONN)               || die "listen: $!";
    logmsg "server started on $NAME";

    my $waitedpid;
    use POSIX ":sys_wait_h";
    sub REAPER {
        my $child;
        while (($waitedpid = waitpid(-1, WNOHANG)) > 0) {
            logmsg "reaped $waitedpid" . ($? ? " with exit $?" : "");
        }
        $SIG{CHLD} = \&REAPER;  # loathe SysV
    }
    $SIG{CHLD} = \&REAPER;

    for ( $waitedpid = 0;
          accept(Client, Server) || $waitedpid;
          $waitedpid = 0, close Client)
    {
        next if $waitedpid;
        logmsg "connection on $NAME";
        spawn sub {
            print "Hello there, it's now ", scalar localtime(), "\n";
            exec("/usr/games/fortune")  || die "can't exec fortune: $!";
        };
    }

    sub spawn {
        my $coderef = shift();
        unless (@_ == 0 && $coderef && ref($coderef) eq "CODE") {
            confess "usage: spawn CODEREF";
        }
        my $pid;
        unless (defined($pid = fork())) {
            logmsg "cannot fork: $!";
            return;
        }
        elsif ($pid) {
            logmsg "begat $pid";
            return; # I'm the parent
        }
        else {
            # I'm the child -- go spawn
        }
        open(STDIN,  "<&Client")    || die "can't dup client to stdin";
        open(STDOUT, ">&Client")    || die "can't dup client to stdout";
        ## open(STDERR, ">&STDOUT") || die "can't dup stdout to stderr";
        exit($coderef->());
    }
```

### TCP Clients with IO::Socket
```
    #!/usr/bin/perl -w
    use IO::Socket;
    my $remote = IO::Socket::INET->new(
                        Proto    => "tcp",
                        PeerAddr => "localhost",
                        PeerPort => "daytime(13)",
                    )
                 || die "can't connect to daytime service on localhost";
    while (<$remote>) { print }
```

#### Interactive Client with IO::Socket
```
    #!/usr/bin/perl -w
    use strict;
    use IO::Socket;

    my ($host, $port, $kidpid, $handle, $line);
    unless (@ARGV == 2) { die "usage: $0 host port" }
    ($host, $port) = @ARGV;
    # create a tcp connection to the specified host and port
    $handle = IO::Socket::INET->new(Proto     => "tcp",
                                    PeerAddr  => $host,
                                    PeerPort  => $port)
               || die "can't connect to port $port on $host: $!";
    $handle->autoflush(1);       # so output gets there right away
    print STDERR "[Connected to $host:$port]\n";

    # split the program into two processes, identical twins
    die "can't fork: $!" unless defined($kidpid = fork());

    if ($kidpid) {
        # Parent
        # copy socket => stdout
        while (defined ($line = <$handle>)) {
            print STDOUT $line;
        }
        kill("TERM", $kidpid);   # send SIGTERM to child
    }
    else {
        # Child
        # copy stdin => socket
        while (defined ($line = <STDIN>)) {
            print $handle $line;
        }
        exit(0);                # just in case
    }
```

If the remote server sends data a byte at time, and you need that data immediately
without waiting for a newline (which might not happen), you may wish to replace
the while loop in the parent with the following:
```
    while (sysread($handle, $buffer, $lenInBytes) == 1) {
        print STDOUT $buffer;
    }
```
**sysread**>>>
sysread FILEHANDLE,SCALAR,LENGTH,OFFSET
Attempts to read LENGTH bytes of data into variable SCALAR from the specified FILEHANDLE, using read(2).
<<<


### TCP Servers with IO::Socket
...

### UDP: Message Passing
...

### SysV IPC
While System V IPC isn't so widely used as sockets, it still has some interesting uses.
However, you cannot use SysV IPC or Berkeley mmap() to have a variable shared amongst several processes.
That's because Perl would reallocate your string when you weren't wanting it to.
You might look into the IPC::Shareable or threads::shared modules for that.

