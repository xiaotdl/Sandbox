#include <iostream>

using namespace std;

void f(const int64_t x) {
  cout << x << endl;
}

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  int x = 100;
  // int* p = &x;
  int* p = nullptr;
  f(p && *p);
  // cout << *p << endl;
  cout << "EOP" << endl;
}

