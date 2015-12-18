#include <iostream>
using namespace std;

#define LENGTH 10
#define WIDTH 5
#define NEWLINE '\n'

// Global variable declaration
int g = 0;

// Function declarition
void func(void);

static int cnt = 10; /* Global var */

int main()
{ 
/* == C++ Variable Scope ==
 * local variable: inside a function or a block
 * formal parameter: in the definition of function parameters
 * global variable: outside of all functions
 */
    // Local variable declaration
    int a, b;
    int g; // local variable will take preference than global var

    // Actual initialization
    a = 10;
    b = 20;
    g = a + b;

    cout << g << endl;

/* Initializing Local and Global vars
 * local var: init required
 * global var: init automatically if not defined
 * <Data Type>    <Initializer>
 * int         -> 0
 * char        -> '\0'
 * float       -> 0
 * double      -> 0
 * pointer     -> NULL
 */


/* == C++ Constants/Literals
 * constant = literal: value that never alter
 * can be data type of int, float, char, string, bool
 * Define constants:
 *     - using `#define` preprocessor
 *     - using `const` keyword, syntax: const type var = value;
 * Note that it is a good programming practice to define constants in CAPITALS.
 */
    int area;

    area = LENGTH * WIDTH;
    cout << area << NEWLINE;

    int A;

    const int L = 10;
    const int W = 5;
    const char N = '\n';

    A = L * W;
    cout << A << N;


/* == C++ Modifier Type ==
 * signed, unsiged, long, short
 */
    short int i;            // a signed short integer
    short unsigned int j;   // an unsigned short integer

    j = 50000;

    i = j;
    cout << i << " " << j << endl;
    // >>>
    // -15536 50000

/* C++ Type Qualifiers
 * const, volatile, restrict
 * const: objects of type const cannot be changed
 * volatile: tells compiler that var value may be changed in ways not explicitly specified by the program
 * restrict: initially the only means by which the object it points to can be accessed.
 */

/* == Storage Classes in C++ ==
 * A storage class defines the scope(visibility) and life-time of variables and/or
 * functions with a C++ Program:
 * auto, register, static, extern, mutable,
 */
    // auto
    // auto is the default storage class for all local vars
    // auto can be used within functions
    int month;
    // same as:
    // auto int month;
    
    // register
    // register is used to define local variables that stored in a register instead of RAM
    // that means the var has a max size equal to the register size (usually one word) and
    // usually cannot have the unary '&' operatore applied to it (as it doesn't have memory location).
    // e.g. cnter
    //
    register int miles;

    // static
    // static instructs the compiler to keep a local va in existence during the life-time of the program
    // instead of creating and destroying it each time it comes into and goes out of scope.
    // Therefore, making local var static allows them to maintain their values between function calls.
    //
    // The static modifier may also be applied to global vars, that will causes the var's scope be restricted
    // to the file it's declared.
    //
    // In C++, when static is used on a class data member, it causes only one copy of that member to be 
    // shared by all objects of its class.
    while (cnt--) {
        func();
    }

    // extern
    // extern is used to give a reference of a global var that is visible to ALL the program files.
    // when extern is used, the var cannot be initialized as it will point the var name at a storage 
    // location that has been previously defined.
    // e.g. extern int count;
    // e.g. extern void write_extern();

    // mutable
    // mutalbe applies only to class objects.
    // It allows a member of an object to override constness. That is, a mutable member can be modified
    // by a const member function.

    return 0;
}

// Function definition
void func(void) {
    static int i = 5; // local static var
    i++;
    cout << "i is " << i;
    cout << " and cout is " << cnt << endl;
}
