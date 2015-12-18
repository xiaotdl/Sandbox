#include <iostream>
#include <ctime>
using namespace std;

const int MAX = 3;

void getSeconds(unsigned long *par);
double getAverage(int *arr, int size);
int * getRandom();

int main()
{ 
/* == C++ Pointers ==
 * Some C++ tasks are performed more easily with pointers,
 * other C++ tasks, such as dynamic memory allocation, cannot be
 * performed without them.
 *
 * Every var is a memory location and every memory location has
 * its address defined which can be accessed using ampersand (&).
 */
    int  var1;
    char var2[10];

    cout << "Address of var1: ";
    cout << &var1 << endl;

    cout << "Address of var2: ";
    cout << &var2 << endl;

/* What are pointers?
 * A pointer is a var whose value is the address of another var.
 * Like any var or constant, you must declare a pointer before using it.
 * syntax: type *var-name;
 * e.g.
 * int    *ip;  //pointer to an integer
 * double *dp;  //pointer to a double
 * float  *fp;  //pointer to a float
 * char   *chp; //pointer to a character
 *
 * Note that the actual data type of the value of all pointers, whether
 * int, float, double, char, or otherwise, is the same, a long hexadecimal
 * number representing a memory address.
 */

/* Using Pointers in C++
 *
 * Note that the actual data type of the value of all pointers, whether
 * int, float, double, char, or otherwise, is the same, a long hexadecimal
 * number representing a memory address.
 * Frequent actions:
 * (a) define a pointer var
 * (b) assign the address of a var to a pointer
 * (c) access the value at the address available in the pointer var (through unary operator *)
 */
    int var = 20;  // actual var declaration
    int *ip;       // pointer var

    ip = &var;     // store address of actual var into pointer var

    cout << "Value of var: ";
    cout << var << endl;

    cout << "Address stored in ip variable: ";
    cout << ip << endl;

    cout << "Value of *ip variable: ";
    cout << *ip << endl;
    cout << endl;

/* == C++ NULL pointer ==
 * It's always a good practice to assign NULL to a pointer var in case
 * you don't have exact address to be assigned.
 * The NULL pointer is a constant with a value of zero defined in several standard libraries.
 */
    int *ptr = NULL;
    cout << "The value of a null pointer is: " << ptr << endl;

    if (ptr) {
        cout << "WARNING: ptr is not NULL!";
    }
    cout << endl;

/* == C++ pointer arithmetic ==
 * ++, --, +, -
 */

/* Incrementing a pointer */
    int var_arr[MAX] = {10, 100, 200};
    int *ptr1;

    ptr1 = var_arr;
    for (int i = 0; i < MAX; i++) {
        cout << "Address of var_arr[" << i << "] : ";
        cout << ptr1 << endl;

        cout << "Value   of var_arr[" << i << "] : ";
        cout << *ptr1 << endl;

        // point to the next location
        ptr1++;
    }
    cout << endl;

/* Decrementing a pointer */
    int *ptr2;
    ptr2 = &var_arr[MAX-1];
    for (int i = MAX; i > 0; i--) {
        cout << "Address of var_arr[" << i << "] : ";
        cout << ptr2 << endl;

        cout << "Value   of var_arr[" << i << "] : ";
        cout << *ptr2 << endl;

        // point to the previous location
        ptr2--;
    }
    cout << endl;

/* Pointer comparisons
 * ==, >, <
 * If p1 and p2 point to variables that are related to each other,
 * such as elements of the same array, then p1 and p2 can be meaningfully compared.
 */
    int *ptr3;

    ptr3 = var_arr;
    int i = 0;
    while (ptr3 <= &var_arr[MAX - 1]) {
        cout << "Address of var_arr[" << i << "] : ";
        cout << ptr3 << endl;

        cout << "Value   of var_arr[" << i << "] : ";
        cout << *ptr3 << endl;

        // point to the previous location
        ptr3++;
        i++;
    }
    cout << endl;

/* == C++ Pointers vs. Arrays ==
 * Pointers and Arrays are strongly related. In fact, they are interchangable
 * in many cases.
 * e.g.
 * array[1]
 * same as >>>
 * *(array + 1)
 * <<<
 */

/* == C++ array of pointers ==
 *
 */
    int var_[MAX] = {10, 100, 200};

    for (int i = 0; i < MAX; i++) {
        cout << "Value of var_[" << i << "] = ";
        cout << var_[i] << endl;
    }


    int *ptr_[MAX]; // this declares ptr as an array of MAX integer pointers
    
    for (int i = 0; i < MAX; i++) {
        ptr_[i] = &var_[i];
    }
    for (int i = 0; i < MAX; i++) {
        cout << "Value of var_[" << i << "] = ";
        cout << *ptr_[i] << endl;
    }


//warning: conversion from string literal to 'char *' is deprecated
//          [-Wc++11-compat-deprecated-writable-strings]
    //char *names[MAX] = {
    //    "Zara",
    //    "Hina",
    //    "Nuha",
    //    "Sara",
    //};

    //for (int i = 0; i < MAX; i++) {
    //    cout << "Value of names[" << i << "] = ";
    //    cout << names[i] << endl;
    //}


/* == C++ Pointer to Pointer (Multiple indiretion) ==
 * syntax: int **var; <= declare a pointer to a pointer of type int
 *       Pointer             Pointer             Variable
 *     -----------         -----------         -----------
 *     | Address |  ---->  | Address |  ---->  |  Value  |
 *     -----------         -----------         ----------- 
 */
    int var_1;
    int *ptr_1;
    int **pptr_1;

    var_1 = 3000;
    ptr_1 = &var_1;
    pptr_1 = &ptr_1;

    cout << "Value of var_1 :" << var_1 << endl;
    cout << "Value available at *ptr_1 :" << *ptr_1 << endl;
    cout << "Value available at **pptr_1 :" << **pptr_1 << endl;


/* == Passing pointers to functions in C++ ==
 */
    unsigned long sec;

    getSeconds( &sec );

    cout << "Number of seconds: " << sec << endl;


    int balance[5] = {1000, 2, 3, 17, 50};
    double avg;

    avg = getAverage( balance, 5 );

    cout << "Average value is: " << avg << endl;

/* == Return pointer from functions in C++ ==
 * syntax:
 * int * myFunction() {...}
 */
    int *p;

    p = getRandom();
    for (int i = 0; i < 10; i++) {
        cout << "*(p + " << i << ") : ";
        cout << *(p + i) << endl;
    }

    return 0;
}


void getSeconds(unsigned long *par) {
    *par = time( NULL );
    return;
}

double getAverage(int *arr, int size) {
    int i, sum = 0;
    double avg;

    for (i = 0; i < size; i++) {
        sum += arr[i];
    }

    avg = double(sum) / size;

    return avg;
}

int * getRandom() {
    static int r[10];

    // set the speed
    srand( (unsigned)time( NULL ) );
    for (int i = 0; i < 10; i++) {
        r[i] = rand();
        cout << r[i] << endl;
    }

    return r;
}




