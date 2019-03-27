#include <iostream>
#include <map>
#include <bitset>

using namespace std;

class Container {
public:
  static std::map<int, std::pair<int, int>> m;

  static void bumpCnt() {
    cnt++;
  }

  static int computeHash(int a, int b) {
    cout << "static computeHash()..." << endl;
    int hash = a % b;
    Container::m[hash] = {a, b};
    return a % b;
  }

  void set(int idx, int p1, int p2) {
    m1[idx] = {p1, p2};
  }

  void get(int idx) const {
    cout << m1.at(idx).first << "->" << m1.at(idx).second << endl;
  }

private:
  // int not_used;
  std::map<int, std::pair<int, int>> m1;

public:
  static int cnt;
  static const uint64_t kTargetingAny;
};

auto Container::cnt = 0;
std::map<int, std::pair<int, int>> Container::m;
const uint64_t Container::kTargetingAny = std::numeric_limits<uint64_t>::max();

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  Container::bumpCnt();
  Container::bumpCnt();
  cout << Container::cnt << endl;

  Container::computeHash(1,2);
  Container::computeHash(3,4);
  for (auto it : Container::m) {
    cout << it.first << "->(" << it.second.first << "," << it.second.second << ")" << endl;
  }

  cout << Container::kTargetingAny << endl;
  {
    std::bitset<64> bs(Container::kTargetingAny);
    cout << bs << endl;
  }
  
  {
    Container c;
    c.set(1, 2, 3);
    c.get(1);
    c.get(2);
  }

  cout << "EOP" << endl;
}

