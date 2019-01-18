#include <iostream>

using namespace std;

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  int *p;
  cout << p << endl;
  if (true) {
    int x[10];
    cout << x << endl;
    p = x;
    cout << p << endl;
  }
  *p = 1; // XXX: SIGSEGV due to stack use out of scope
  cout << p << endl;
}

