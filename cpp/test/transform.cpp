#include <iostream>
#include <vector>

using namespace std;

enum class Status {
  GREEN = 0,
  YELLO = 1,
  RED = 2,
};

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {

  Status s;
  cout << (int)s << endl;
  cout << "EOP" << endl;
}

