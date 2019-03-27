#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>


using namespace std;

namespace util {
  // dump int
  string toString(int x) {
    return std::to_string(x);
  }

  // dump map<int, int>
  string toString(const std::map<int, int>& map) {
    stringstream ss;
    ss << "map(";
    if (map.size() > 0) {
      auto it = map.begin();
      ss << it->first << "->" << toString(it->second);
      while (++it != map.end()) {
        ss << ", " << it->first << "->" << toString(it->second);
      }
    }
    ss << ")";
    return ss.str();
  }

  // dump map<int, vector<int>>
  string toString(std::map<int, std::vector<int>> m) {
    stringstream ss;
    for (auto mItr : m) {
      ss << mItr.first << "->" << "[";
      if (mItr.second.size() > 0) {
        ss << mItr.second[0];
        for (int i = 1; i < mItr.second.size(); i++) {
          ss << ", " << mItr.second[i];
        }
      }
      ss << "]" << "\n";
    }
    return ss.str();
  }

  // dump set<int>
  template <class Container>
  std::string toString(Container container) {
    stringstream ss;
    ss << std::string(typeid(container).name()) << "(";
    if (container.size() > 0) {
      auto it = container.begin();
      ss << *it;
      while (++it != container.end()) {
        ss << ", " << *it;
      }
    }
    ss << ")";
    return ss.str();
  }

  // dump map<int, set<int>>
  string toString(std::map<int, set<int>> map) {
    stringstream ss;
    ss << "map(";
    if (map.size() > 0) {
      auto it = map.begin();
      ss << it->first << "->" << toString(it->second);
      while (++it != map.end()) {
        ss << ", " << it->first << "->" << toString(it->second);
      }
    }
    ss << ")";
    return ss.str();
  }
   

  template <class Container>
  std::string printValueSizeReversed(std::map<int, Container> m) {
    std::string s;
    for (auto it = m.rbegin(); it != m.rend(); it++) {
      s += "k:" + std::to_string(it->first) + "->"
         + "v:" + std::to_string(it->second.size()) + "|";
    }
    return s;
  }
}

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  {
    std::map<int, std::vector<int>> m;
    m[0] = {1,2,4};
    m[1] = {};
    m[2] = {99,100};
    cout << m.size() << endl;
    cout << util::printValueSizeReversed<std::vector<int>>(m) << endl;
    cout << util::toString(m) << endl;

    auto itr = m.find(2);
    if (itr != m.end()) {
      cout << "key:" << itr->first << endl;
      cout << "val.size():" << itr->second.size() << endl;
    }
  }

  {
    std::map<int, int> m;
    m[0] = 0;
    m[1] = 100;
    m[2] = 200;
    cout << "toString: " << util::toString(m) << endl;
  }

  {
    std::map<int, set<int>> m;
    m[0] = {0,0,2};
    m[1] = {1,1,1};
    m[2] = {1,1,2,2,3,3};
    cout << "toString: " << util::toString(m) << endl;
  }

  {
    std::map<int, int> m = {{1,1}, {2,2}};
    cout << "toString: " << util::toString(m) << endl;
  }

  {
    std::unique_ptr<std::map<int, int>> m = std::make_unique<std::map<int, int>>();
    auto it = m->find(1);
    if (it != m->end()) {
      cout << "found!" << endl;
    } else {
      cout << "not found!" << endl;
    }
  }

  {
    std::map<int, int> m = {{1,1}, {2,2}, {3,3}};
    std::vector<int> values;
    values.reserve(m.size());
    for (const auto& it : m) {
      values.push_back(it.second);
    }
    std::sort(values.begin(), values.end());
    cout << "values: " << util::toString(values) << endl;
  }
}
