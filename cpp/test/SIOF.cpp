#include <iostream>

using namespace std;

// http://www.cs.technion.ac.il/users/yechiel/c++-faq/static-init-order-on-first-use.html
// Problem: static initialization order fiasco(SIOF)
// Solution: Use the "construct on first use(COFU)" idiom, which simply means to wrap your static object inside a function.
int& f() {
  static int x = 8;
  cout << &x << endl;
  return x;
}

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  cout << &f() << endl;
  cout << "EOP" << endl;
}

