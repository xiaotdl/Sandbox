#include <iostream>

using namespace std;

// &: ampersand

// Type:
// int, float, MyClass
// T
// T&: reference to Type
// T*: pointer to Type
//


// Operation:
// &O: get pointer/address from object
// *P: get object by deref pointer/address

// pointer/address size
// int64_t == 8 bytes

// T** var; declares a pointer to a pointer
// **var;   references the content of a pointer, which in itself points to a pointer

// pointer
void f2(int* x) {
  *x = 1;
  cout << "f2:" << *x << endl;
}

void f1() {
  int x = 0;
  f2(&x);
  cout << "f1:" << x << endl;
}

// reference
void f4(int& x) {
  x = 1;
  cout << "f4:" << x << endl;
}

void f3() {
  int x = 0;
  f4(x);
  cout << "f3:" << x << endl;
}

// big objects
// struct == class with every func/fields public
struct BigData {
  BigData() {}; // constructor
  ~BigData() {}; // destructor
  int data[100] = {};
  int size = 100; // member variable
  int getSize() { // member function
    return size;
  };
};

void f5(BigData bd) {
  cout << "f5: " << &bd << endl;
  cout << bd.size << endl;
  cout << bd.getSize() << endl;
}

void f6(BigData& bd) {
  cout << "f6: " << &bd << endl;
  cout << bd.size << endl;
  cout << bd.getSize() << endl;
}

void f7(BigData* bd) {
  cout << "f7: " << bd << endl;
  cout << (*bd).size << endl;
  cout << (*bd).getSize() << endl;
  cout << bd->size << endl; // same as above, just a syntactic sugar
  cout << bd->getSize() << endl;
}


// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  {
    // pointer example
    f1();
  }
  {
    // reference example
    f3();
  }
  {
    // big data pass by value, by ref, by pointer
    BigData bd; // create instance in current stack
    cout << "&bd:" << &bd << endl;
    f5(bd); // pass by value; make copy
    f6(bd); // pass by ref; no copy
    f7(&bd); // pass by ptr; no copy
  }
  {
    BigData bd;
    bd.size = 99;      // addr = &bd | val = {}
    BigData** p1;      // addr = p1  | val = ?
    BigData* p2;       // addr = p2  | val = ?
    p2 = &bd;          // addr = p2  | val = &bd
    p1 = &p2;          // addr = p1  | val = &p2
    cout << "bd.size: " << bd.size << endl;
    cout << "(**p1).size: " << (**p1).size << endl;
    cout << "(*p1)->size: " << (*p1)->size << endl;
  }
  {
    // BigData* bdPtr = new BigData(); // create instance in heap
    // free(bdPtr);

    // smart pointer: unique ptr, shared ptr
    // unique_ptr<BigData> bdUptr = make_unique<BigData>(); 
    auto bdUptr = make_unique<BigData>();  // same as above
  }
  {
    // int main(int argc, char* argv[]);
    // is equivalent to:
    // int main(int argc, char** argv);
    //
    // argv is a pointer to an array of char*
    //
    // the index operator [] is just another way of performing pointer arithmetic
    // foo[i]
    // is equivalent to:
    // *(foo + i)
    //
    // T**: It might be a matrix (an array of arrays) or an array of strings (a char array), etc.
  }
  cout << "EOP" << endl;
}

