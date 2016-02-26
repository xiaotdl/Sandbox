/* C Preprocessor (CPP):
 * It's not a part of the compiler, but is a seperate step in compilation process.
 * In simple terms, it's a just a text substitution tool and it instructs 
 * compiler to do required pre-processing before the actual compilation.
 * All preprocessor commands starts with a hash symbol (#).
 */

// e.g.
// #define  - substitutes a preprocessor macro
// #include - inserts a particular head from another file
// #undef   - undefines a preprocessor macro
// #ifdef   - returns true if this macro defined
// #ifndef  - returns true if this macro not defined
// #if
// #else
// #elif
// #endif
// #error   - prints error message on stderr
// #pragma  - issues special commands to the compiler, using a standardized method

#include <stdio.h> // tell CPP to get stdio.h from System Libraris
#include "test_preprocessor.h" // get test_preprocessor.h from current dir

#define MAX_ARRAY_SIZE 20 // define constants to increase readability

#undef FILE_SIZE // tells CPP to undefine existing FILE_SIZE and redefines it
#define FILE_SIZE 42

#ifdef DEBUG
    /* your debugging statements here */
#endif

// == predefined macros ==
// e.g. __XXXX__

// The Macro Continuation (\) Operator
// The Stringize (#) Operator - converts a macro param into a string constant
#define message_for(a, b)  \
            printf(#a " and " #b ": We love you!\n")

// The Token Pasting (##) Operator
#define tokenpaster(n) \
    printf ("token" #n " = %d\n", token##n)
// same as >>>
//  printf ("token34 = %d", token34);
// <<<

// The Defined() Operator
#if !defined (MESSAGE)
    #define MESSAGE "You wish!"
#endif

// Parameterized Macros
#define MAX(x,y) ((x) > (y) ? (x) : (y))


int main() {
    printf("File :%s\n", __FILE__ );
    printf("Date :%s\n", __DATE__ );
    printf("Time :%s\n", __TIME__ );
    printf("Line :%d\n", __LINE__ );
    printf("ANSI :%d\n", __STDC__ );

    message_for(Carole, Debra);

    int token34 = 40;
    tokenpaster(34);
    printf("Here is the message: %s\n", MESSAGE);

    printf("Max between 20 and 10 is: %d\n", MAX(10, 20));

    return 0;
}
