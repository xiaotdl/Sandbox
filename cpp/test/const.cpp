#include <iostream>

using namespace std;

struct MyStruct {
  int x = 1;
  int y = 2;
};

class SomeClass {
public:
  void maybeModify();
  void dontModify() const;
};

// class SomeClass2 {
// public:
//   void dontModify() const {
//     val = 100; // XXX: error: cannot assign to non-static data member within const member function 'dontModify'
//   }
// int val = 0;
// };

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  //  == Syntactic const ==
  // {
  //   const int x = 1;
  //   x = 2; // XXX: error: cannot assign to variable 'x' with const-qualified type 'const int'
  // }


  // {
  //   MyStruct const o;
  //   o.x = 100; // XXX: error: cannot assign to variable 'o' with const-qualified type 'const MyStruct'
  //   o.y = 200;
  // }


  // {
  //   SomeClass const someObject{};
  //   someObject.dontModify();  // OK
  //   someObject.maybeModify(); // XXX: error: member function 'maybeModify' not viable: 'this' argument has type 'const SomeClass', but function is not marked const
  // }


  // {
  //   int i = 0; 
  //   int j = 1;
  //   int *const pi = &i;
  //   *pi = 33; //OK - i is now 33
  //   pi = &j; //ERROR - pi is const, XXX: error: cannot assign to variable 'pi' with const-qualified type 'int *const'
  // }


  // == Semantic const ==
   
  cout << "EOP" << endl;
}

