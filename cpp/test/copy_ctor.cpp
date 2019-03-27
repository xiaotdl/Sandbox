#include <iostream>

using namespace std;
struct A {
  A(int val) : val(val) {}

  A& operator=(A other) = delete;
  int val = 100;
};

struct B {
  B(int val)
  : a(make_unique<A>(val)) {
  }
  B() {
  }

  std::unique_ptr<A> a = nullptr;
};

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  B b(99);
  cout << b.a->val << endl;
  cout << "EOP" << endl;
}

