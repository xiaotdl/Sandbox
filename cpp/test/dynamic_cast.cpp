#include <iostream>

using namespace std;

enum class Type {
  A = 0,
  B = 1,
};

class A {
 public:
  virtual ~A() {}
  Type getType() {
    return Type::A;
  }
};

class B : public A {
 public:
  Type getType() {
    return Type::B;
  }
  void doSth() {
    cout << "doing..." << endl;
  }
};

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  A* a = new B();
  cout << std::to_string((int)a->getType()) << endl;
  // a->doSth(); // error: no member named 'doSth' in 'A'

  // B* b = dynamic_cast<B*>(a);
  // cout << std::to_string((int)b->getType()) << endl;
  // b->doSth();

  dynamic_cast<B*>(a)->doSth();
  // a->doSth(); // error: no member named 'doSth' in 'A'

  cout << "EOP" << endl;
}

