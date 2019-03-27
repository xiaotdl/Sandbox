#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;

using AdId = int64_t;

struct A {};
struct B {};

struct MyClass {
  MyClass(A a) : a(a) {};
  A a;
  B b;
};


// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  A a;
  MyClass c1(a);
  MyClass c2(a);
  std::vector<std::shared_ptr<MyClass>> v;
  cout << sizeof(uint64_t) << endl;

  cout << (5 >> 2) << endl;

  cout << "E" "O" "P"<< endl;
}

