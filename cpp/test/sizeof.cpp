#include <iostream>

// sizeof():
// return size in bytes

using namespace std;

struct Empty {};
struct Base { int a; };
struct Derived : Base { int b; };
struct Bit { unsigned bit: 1; };

int main()
{
    Empty e;
    Derived d;
    Base& b = d;
    [[maybe_unused]] Bit bit;
    int a[10];
    std::cout << "size of empty class:              " << sizeof e        << "\n"
              << "size of pointer:                  " << sizeof &e       << "\n"
//            << "size of function:                "  << sizeof(void())  << "\n" // error
//            << "size of incomplete type:         "  << sizeof(int[])   << "\n" // error
//            << "size of bit field:               "  << sizeof bit.bit  << "\n" // error
              << "size of array of 10 int:         "  << sizeof(int[10]) << "\n"
              << "size of array of 10 int (2):     "  << sizeof a        << "\n"
              << "length of array of 10 int:       "  << ((sizeof a) / (sizeof *a)) << "\n"
              << "length of array of 10 int (2):   "  << ((sizeof a) / (sizeof a[0])) << "\n"
              << "size of the Derived:              " << sizeof d        << "\n"
              << "size of the Derived through Base: " << sizeof b        << "\n";

    cout << "Size of char : " << sizeof(char)  
      << " byte" << endl; 
    cout << "Size of int : " << sizeof(int) 
      << " bytes" << endl; 
    cout << "Size of short int : " << sizeof(short int)  
      << " bytes" << endl; 
    cout << "Size of long int : " << sizeof(long int)  
       << " bytes" << endl; 
    cout << "Size of signed long int : " << sizeof(signed long int) 
       << " bytes" << endl; 
    cout << "Size of unsigned long int : " << sizeof(unsigned long int)  
       << " bytes" << endl; 
    cout << "Size of int32_t : " << sizeof(int32_t) 
      << " bytes" << endl; 
    cout << "Size of int64_t : " << sizeof(int64_t) 
      << " bytes" << endl; 
    cout << "Size of float : " << sizeof(float)  
       << " bytes" <<endl; 
    cout << "Size of double : " << sizeof(double)  
       << " bytes" << endl; 
    cout << "Size of wchar_t : " << sizeof(wchar_t)  
       << " bytes" <<endl; 
      
}

// >>>
// size of empty class:              1
// size of pointer:                  8
// size of array of 10 int:         40
// size of array of 10 int (2):     40
// length of array of 10 int:       10
// length of array of 10 int (2):   10
// size of the Derived:              8
// size of the Derived through Base: 4
