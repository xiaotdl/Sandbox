#include <iostream>

using namespace std;

namespace xili {
  void f() {
    cout << "hello.." << endl;
  }
}

namespace a_b {}

// dash is not allowed in namespace naming
// namespace a-b {} // XXX: error: expected ';' after top level declarator

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  xili::f();
  cout << "EOP" << endl;
}

