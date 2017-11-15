NAME
     tee -- pipe fitting

SYNOPSIS
     tee [-ai] [file ...]

-a, --append
    Append to the given FILEs. Do not overwrite.
-i, --ignore-interrupts
    Ignore interrupt signals.

# Example 1: Write output to stdout, and also to a file
# The following command (with the help of tee command) writes the output both to the screen (stdout) and to the file.
$ ls | tee <file>
# You can also write the output to multiple files as shown below.
$ ls | tee <file1> <file2> <file3>

# Example 2: Write the output to two commands
# You can also use tee command to store the output of a command to a file and redirect the same output as an input to another command.
$ crontab -l | tee crontab-backup.txt | sed 's/old/new/' | crontab –


