#include <iostream>

using namespace std;

struct B;

struct A {
  A() = default;

  A(int val)
  : b(make_unique<B>(val)) {
  }

  std::unique_ptr<B> b = nullptr;
};

struct B {
  B() {
      cout << "ctor" << endl;
  }

  B(int val) : val(val) {
      cout << "custom ctor" << endl;
  }

  B(const B& other) {
      cout << "copy ctor" << endl;
  }

  B& operator=(const B& other) {
      cout << "copy assignment" << endl;
      return *this;
  }

  int val = 100;
};

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  A a(99);
  cout << a.b->val << endl;

  cout << "B b(100);" << endl;
  B b(100);
  auto bup = std::make_unique<B>(100);

  cout << "B b1(b);" << endl;
  B b1(b);  // XXX: copy ctor:   B(const B& other) = delete;
  auto b1up = std::make_unique<B>(*bup);

  cout << "B b2;" << endl;
  B b2;     // XXX: ctor:        B() = delete; 
  auto b2up = std::make_unique<B>();

  cout << "b2 = b;" << endl;
  b2 = b;   // XXX: copy assign: B& operator=(const B& other) = delete;
  *b2up = *bup;

  cout << "B b3 = b;" << endl;
  B b3 = b; // XXX: copy ctor:   B(const B& other) = delete;
  auto b3up = std::make_unique<B>(*bup);

  cout << "EOP" << endl;
}

