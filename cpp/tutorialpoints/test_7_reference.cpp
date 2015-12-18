#include <iostream>
using namespace std;

void swap(int& x, int&y);

double vals[] = {10.1, 12.6, 33.1, 24.1, 50.0};

double& setValues( int i ) {
    return vals[i];  // return a reference to the ith element
}

int main()
{ 
/* == C++ References ==
 * A reference variable is an alias for an already existing variable.
 * C++ References vs. Pointers:
 *  - You cannot have NULL references. A reference is always connected to a 
 *    legitimate piece of storage.
 *  - Once a reference is initialized to an object, it cannot be changed to
 *    refer to another object. Pointers can be pointed to another obj at any time.
 *  - A reference must be initialized when it is created. Pointers can be
 *    initialized at any time.
 *  e.g.
 *  int  i = 17;
 *  int& r = i;
 *
 *  References are usually used for function argument lists and return values.
 */
    int    i;
    double d;

    int&    r = i;
    double& s = d;

    i = 5;
    cout << "Value of i : " << i << endl;
    cout << "Value of i reference: " << r << endl;

    d = 11.7;
    cout << "Value of d : " << d << endl;
    cout << "Value of d reference: " << s << endl;

/* == References as parameters in C++ ==
 * call by reference
 */
    int a = 100;
    int b = 200;

    cout << "Before swap, value of a :" << a << endl;
    cout << "Before swap, value of b :" << b << endl;
 
    /* calling a function to swap the values.*/
    swap(a, b);
 
    cout << "After swap, value of a :" << a << endl;
    cout << "After swap, value of b :" << b << endl;

/* == Returning values by reference in C++ ==
 */
    cout << "Value before change" << endl;
    for (int i = 0; i < 5; i++) {
        cout << "vals[" << i << "] = ";
        cout << vals[i] << endl;
    }

    setValues(1) = 20.23;
    setValues(3) = 70.8;

    cout << "Value after change" << endl;
    for (int i = 0; i < 5; i++) {
        cout << "vals[" << i << "] = ";
        cout << vals[i] << endl;
    }

    return 0;
}

void swap(int& x, int& y) {
    int temp;

    temp = x;
    x = y;
    y = temp;

    return;
}

// It is legal to return a reference to local var.
// You can always return a reference on a static variable.
int& func() {
   int q;
   //! return q; // Compile time error
   static int x;
   return x;     // Safe, x lives outside this scope
}


