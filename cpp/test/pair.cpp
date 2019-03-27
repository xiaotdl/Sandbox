#include <iostream>
#include <map>
#include <vector>

using namespace std;

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  {
    std::pair<int, int> p(1, 2);
    cout << p.first << "," << p.second << endl;
  }

  {
    std::map<int, std::pair<int, int>> m;
    m[0] = {3,4};
    cout << m[0].first << "," << m[1].second << endl;
  }

  {
    std::map<int, std::vector<int>> m;
    m[0].push_back(0);
    m[0].push_back(1);
    cout << m[0].size() << endl;
  }
  cout << "EOP" << endl;
}

