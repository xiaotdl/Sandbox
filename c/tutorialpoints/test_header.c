// Two types of header files:
// 1. the files that programmer writes    -> #include "file"
// 2. the files that comes with compiler  -> #include <file>

// A simple practice in C or C++ is that:
// we keep all the constants, macros, system wide globle vars, and function prototypes in header files and include that file when needed.

#if SYSTEM_1
   # include "system_1.h"
#elif SYSTEM_2
   # include "system_2.h"
#elif SYSTEM_3
   ...
#endif
