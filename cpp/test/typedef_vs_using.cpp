#include <iostream>

// REF:
// http://www.cplusplus.com/doc/tutorial/other_data_types/
//
// Both aliases defined with typedef and aliases defined with using are semantically equivalent.
// The only difference being that typedef has certain limitations in the realm of templates that using has not.
// Therefore, using is more generic, although typedef has a longer history and is probably more common in existing code.
//
// syntax:
//   typedef existing_type new_type_name;
//   using new_type_name = existing_type;

// e.g.
typedef unsigned char BYTE;
using BYTE = unsigned char;

using namespace std;

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  BYTE b;
  cout << sizeof(b) << endl;
  cout << "EOP" << endl;
}

