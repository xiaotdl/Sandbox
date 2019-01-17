#include <iostream>

using namespace std;

struct Point {
  Point(int x, int y) : x(x), y(y) {}
  int x;
  int y;
};

//This function returns a new object, not a reference to the object
Point makePoint() {
  Point p(1, 2);
  cout << &p << endl;
  return p;
}

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  auto p = makePoint();
  cout << &p << endl;
  cout << "EOP" << endl;

}

