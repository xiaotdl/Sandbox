#include <iostream>

using namespace std;

class Klass {
public:
  Klass() {
    cout << "constructed" << endl;
    cout << this << endl;
  }
  Klass(const Klass& kls) {
    cout << "copy constructed" << endl;
  }
};

std::unique_ptr<Klass> makeKlass() {
  return make_unique<Klass>();
  // return nullptr;
}

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  // std::unique_ptr<Klass> up = makeKlass(); // can't pass into shared_ptr if explicitly constructed unique_ptr

  std::shared_ptr<Klass> sp(makeKlass());
  cout << sp.get() << endl;
  if (sp) {
    // if makeKlass() return make_unique<Klass>();
    cout << "sp!!" << endl;;
  } else {
    // if makeKlass() return nullptr
    cout << "NA!!" << endl;;
  }

  cout << "EOP" << endl;
}

