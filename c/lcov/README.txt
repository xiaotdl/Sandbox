
== Brief Description of gcov Data Files ==
# Ref:
# https://gcc.gnu.org/onlinedocs/gcc/Gcov-Data-Files.html

gcov uses two files for profiling. The names of these files are derived from the original object file by substituting the file suffix with either .gcno, or .gcda. The files contain coverage and profile data stored in a platform-independent format. The .gcno files are placed in the same directory as the object file. By default, the .gcda files are also stored in the same directory as the object file, but the GCC -fprofile-dir option may be used to store the .gcda files in a separate directory.

The .gcno notes file is generated when the source file is compiled with the GCC -ftest-coverage option. It contains information to reconstruct the basic block graphs and assign source line numbers to blocks.

The .gcda count data file is generated when a program containing object files built with the GCC -fprofile-arcs option is executed. A separate .gcda file is created for each object file compiled with this option. It contains arc transition counts, value profile counts, and some summary information.

P.S.
1) .gcno and .gcda files have to be put in the same dir (gcov n lcov doesn't provide option to specify them differently).
2) path needs to be preserved? 


== Demo ==
# Ref:
# [整理] gcov lcov 覆盖c/c++项目入门
# http://www.cnblogs.com/turtle-fly/archive/2013/01/09/2851474.html
[] - newly created file

vagrant@xili-dev-fit-win-2:~/lcov_example$ ls
[fib.c]


vagrant@xili-dev-fit-win-2:~/lcov_example$ gcc fib.c -o fib --coverage
vagrant@xili-dev-fit-win-2:~/lcov_example$ ls
[fib]  fib.c  [fib.gcno]


vagrant@xili-dev-fit-win-2:~/lcov_example$ ./fib
fibonnaci(0) = 0
fibonnaci(1) = 1
fibonnaci(2) = 1
fibonnaci(3) = 2
fibonnaci(4) = 3
fibonnaci(5) = 5
fibonnaci(6) = 8
fibonnaci(7) = 13
fibonnaci(8) = 21
fibonnaci(9) = 34
fibonnaci(10) = 55
vagrant@xili-dev-fit-win-2:~/lcov_example$ ls
fib  fib.c  [fib.gcda]  fib.gcno


vagrant@xili-dev-fit-win-2:~/lcov_example$ gcov fib.c
File 'fib.c'
Lines executed:100.00% of 12
Creating 'fib.c.gcov'
vagrant@xili-dev-fit-win-2:~/lcov_example$ ls
fib  fib.c  [fib.c.gcov]  fib.gcda  fib.gcno


vagrant@xili-dev-fit-win-2:~/lcov_example$ lcov -c -d . -o fib.info
Capturing coverage data from .
Found gcov version: 4.9.2
Scanning . for .gcda files ...
Found 1 data files in .
Processing fib.gcda
Finished .info-file creation


vagrant@xili-dev-fit-win-2:~/lcov_example$ genhtml fib.info -o fib_result
Reading data file fib.info
Found 1 entries.
Found common filename prefix "/home/vagrant"
Writing .css and .png files.
Generating output.
Processing file lcov_example/fib.c
Writing directory view page.
Overall coverage rate:
  lines......: 100.0% (12 of 12 lines)
  functions..: 100.0% (2 of 2 functions)

