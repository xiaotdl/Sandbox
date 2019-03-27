#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  std::vector<int> v1 = {1,3,5};
  std::vector<int> v2 = {1,3,5};
  cout << (v1 == v2) << endl;
  assert(v1 == v2);

  cout << "EOP" << endl;
}

