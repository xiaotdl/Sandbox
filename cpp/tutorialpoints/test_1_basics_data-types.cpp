#include <iostream>
using namespace std;

// Variable declaration:
extern int a, b;
extern int c;
extern float f;

// function declaration
int func();

int main()
{ 
/* == C++ Basics ==
 * C++ program is considered to be a collection of objects
 * that communicate via invoking each other's methods.
 * - Object
 * - Class
 * - Methods
 * - Instance Variables
 */
    // print sth
    cout << "Hello Wendi" << endl;


/* == C++ Data Types ==
 * bool, char, int, float, double, void, wchar_t
 * Type modifiers:
 * signed, unsigned, short, long
 */
    // endl inserts a new line
    // sizeof() operator to get size of various data types.
    cout << "Size of int : " << sizeof(int) << endl;

    // typedef declaration
    // typedef type newname;
    typedef int feet; // tell compiler feet is another name of int
    feet distance; // declare a new int variable


/* == Enumerated Types ==
 * syntax: enum enum-name { list of names  } var-list;
 * e.g. enum color { red, green, blue } c; // red, green, blue = 0, 1, 2
 * c = blue;
 * By default each name has a increasing value starting from 0. 
 * But you can give a name a specific value
 * e.g. enum color { red, green=5, blue }; // red, green, blue = 1, 5, 6 
 * 
 * C++ also allows to define various other types of vars, like:
 * Enumeration, pointer, array, Refeerence, Data structure, Classes
 */
    enum color { red, green, blue } x; // red, green, blue = 0, 1, 2
    cout << red << endl;
    cout << green << endl;
    cout << blue << endl;
    cout << x << endl;

/* Variable definition in C++
 * syntax: type variable_list;
 * type must be a valic C++ data type including char, w_char, int,
 * float, double, or any user-defined object, etc.
 * e.g.
 * int    i, j, k;
 * char   c, ch;
 * float  f, salary;
 * double d;
 *
 * Variable can be initialized along with declarition
 * e.g.
 * extern int d = 3, f = 5;
 * int d = 3, f = 5; 
 * byte z = 22;
 * char x = 'x';
 */
    // Variable definition:
    int a, b;
    int c;
    float f;
 
    // actual initialization
    a = 10;
    b = 20;
    c = a + b;
 
    cout << c << endl ;

    f = 70.0/3.0;
    cout << f << endl ;

    int i = func();
    cout << i << endl ;

/* Lvalue: expression that refers to memory location
 * Rvalue: data value that is stored at some address in memory.
 */


    return 0;
}


// function definition
int func()
{
    return 0;
}
