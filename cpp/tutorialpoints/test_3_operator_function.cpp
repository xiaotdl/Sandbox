#include <iostream>
using namespace std;

void swap_call_by_value(int x, int y);
void swap_call_by_pointer(int *x, int *y);
void swap_call_by_reference(int &x, int &y);


int main()
{ 
/* == C++ operators ==
 * Arithmetic:    +, -, *, /, %, ++, --
 * Relational:    ==, !=, >, <, >=, <=
 * Logical:       &&, ||, !
 * Bitwise:       &, |, ^, ~, <<, >>
 * Assignment:    =, +=, -=, *=, /=, %=, <<=, >>=, &=, ^=, |=
 * Misc:          sizeof(), cond?x:y,',', '.', ->, cast, &, *
 */

/* Operator precedence and order
 * Category         Operator                           Associativity
 * Postfix          () [] -> . ++ --                   -->
 * Unary            + - ! ~ ++ -- (type) * & sizeof    <--
 * Multiplicative   * / %                              -->
 * Additive         + -                                -->
 * Shift            << >>                              -->
 * Relational       < <= > >=                          -->
 * Equality         == !=                              -->
 * Bitwise AND      &                                  -->
 * Bitwise XOR      ^                                  -->
 * Bitwise OR       |                                  -->
 * Logical AND      &&                                 -->
 * Logical OR       ||                                 -->
 * Conditional      ?:                                 <--
 * Assignment       = += -= *= /= %= >>= <<= &= ^= |=  <--
 * Comma            ,                                  -->
 */

/* == C++ Functions ==
 * Every C++ program has at least one function, which is main()
 *
 * A function declaration tells the compiler about 
 * 1) function name 2) return type 3) parameter
 *
 * A function definition provides the actual body of the function.
 *
 * A function is aka a method, or a sub-routine, or a procedure etc.
 * e.g.
 * return_type function_name (parameter list) {
 *     body of the functiona
 * }
 */

/* C++ Functional Arguments
 * While calling a function, there are 3 ways that args passed to a function:
 *  - call by value
 *  - call by pointer
 *  - call by reference
 * By default, C++ uses call by value to pass args.
 */
    // call by value
    int a = 100;
    int b = 200;
    cout << "Before swap_call_by_value, a=" << a << " b=" << b << endl;
    swap_call_by_value(a, b);
    cout << "After  swap_call_by_value, a=" << a << " b=" << b << endl;
    cout << endl;

    // call by pointer
    a = 100;
    b = 200;
    cout << "Before swap_call_by_pointer, a=" << a << " b=" << b << endl;
    swap_call_by_pointer(&a, &b);
    cout << "After  swap_call_by_pointer, a=" << a << " b=" << b << endl;
    cout << endl;

    // call by reference
    a = 100;
    b = 200;
    cout << "Before swap_call_by_reference, a=" << a << " b=" << b << endl;
    swap_call_by_reference(a, b);
    cout << "After  swap_call_by_reference, a=" << a << " b=" << b << endl;
    cout << endl;

/* Default Values for Parameters
 * e.g.
 * int sum(int a, int b=20) {
 *     ...
 * }
 */


    return 0;
}

void swap_call_by_value(int x, int y) {
    int temp;

    temp = x;
    x = y;
    y = temp;

    return;
}

void swap_call_by_pointer(int *x, int *y) {
    int temp;

    temp = *x;
    *x = *y;
    *y = temp;

    return;
}

void swap_call_by_reference(int &x, int &y) {
    int temp;

    temp = x;
    x = y;
    y = temp;

    return;
}
