#include <iostream>
#include <sstream>
#include <set>

using namespace std;

namespace util {
  // dump set<int>
  std::string toString(std::set<int> set) {
    stringstream ss;
    ss << "set(";
    if (set.size() > 0) {
      auto it = set.begin();
      ss << *it;
      while (++it != set.end()) {
        ss << ", " << *it;
      }
    }
    ss << ")";
    return ss.str();
  }
}

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  std::set<int> set = {1,2,3,3};
  cout << "set.size(): " << set.size() << endl;
  cout << "toString: " << util::toString(set) << endl;
  cout << "EOP" << endl;
}

