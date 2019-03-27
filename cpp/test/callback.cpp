#include <iostream>

typedef void (*callback1) (void);

using namespace std;

void sing() {
  cout << "lalala~" << endl;
}

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  {
    typedef void (*callback) (void);
    callback cb = sing;
    cb();
  }

  {
    using callback = void(*)(void);
    cout << &sing << endl;
    callback cb = sing;
    cout << cb << endl;
    cb();
  }

  {
    using callback = void(&)(void);
    callback cb = sing;
    cb();
  }

  cout << "EOP" << endl;
}

