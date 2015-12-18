$ cat file
Cygwin
Unix
Linux
Solaris
AIX

$ sed '/Unix/{n;s/.*/hi/}' file
Cygwin
Unix
hi
Solaris
AIX
