#include <iostream>

using namespace std;

struct Container {};

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  Container c;
  cout << typeid(c).name() << endl;
  cout << "EOP" << endl;
}

