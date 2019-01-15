#include <iostream>

using namespace std;


// REF: https://www.geeksforgeeks.org/typedef-versus-define-c/
// typedef vs. #define
//   * typedef is limited to giving symbolic names to types only, whereas #define can be used to define alias for values as well.
//     e.g. you can define 3.14 as PI, etc.
//   * typedef interpretation is performed by the compiler, whereas #define statements are performed by preprocessor.
//   * typedef should be terminated with semicolon, whereas #define should not be.
//   * typedef is actual definition of a new type, whereas #define will just copy-paste the definition values at the point of use.
//   * typedef follows the scope rule which means if a new type is defined in a scope(inside a function), then the new type name will only be visible till the scope is there.
//     whereas #define, when preprocessor encounters #define, it replaces all the occurences after that (no scope rule is followed)

// Tip: use typedef to define type
// #include <stdio.h>
// typedef char* ptr;
// #define PTR char*
// int main()
// {
//     ptr a, b, c;
//     PTR x, y, z;
//     printf("sizeof a:%u\n" ,sizeof(a) );
//     printf("sizeof b:%u\n" ,sizeof(b) );
//     printf("sizeof c:%u\n" ,sizeof(c) );
//     printf("sizeof x:%u\n" ,sizeof(x) );
//     printf("sizeof y:%u\n" ,sizeof(y) );
//     printf("sizeof z:%u\n" ,sizeof(z) );
//     return 0;
// }
// Output:
// sizeof a:8
// sizeof b:8
// sizeof c:8
// sizeof x:8
// sizeof y:1
// sizeof z:1


// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  // 1. typedef
  // typedef: typedef is used to give data type a new name

  // e.g.
  // After this line, BYTE can be used in place of unsigned char
  typedef unsigned char BYTE;

  BYTE b1, b2;
  b1 = 'a';
  b2 = 'b';
  cout << b1 << endl;
  cout << b2 << endl;

  // 2. #define
  // #define: is a C directive which is used to #define alias

  // e.g.
  // After this line, HYD is replaced by "Hyperabad"
  #define HYD "Hyperabad"
  cout << HYD << endl;

  cout << "EOP" << endl;
}
 

