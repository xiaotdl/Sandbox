#include <iostream>
#include <map>

using namespace std;


template <class M, class K = typename M::key_type>
typename M::mapped_type* mapGetPtr(M& container, const K& key) {
  auto it = container.find(key);
  if (it != container.end()) {
    return &(it->second);
  } else {
    return nullptr;
  }
}

template <class M, class K = typename M::key_type>
const typename M::mapped_type* mapGetPtr(const M& container, const K& key) {
  auto it = container.find(key);
  if (it != container.end()) {
    return &(it->second);
  } else {
    return nullptr;
  }
}

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  std::map<int, int> m; 
  m[1];
  m[2];
  for (const auto& it : m) {
    cout << it.first << "->" << it.second << endl;
    cout << it.first << ": " << *mapGetPtr(m, it.first) << endl;
    cout << it.get().get() << endl;
  }

  cout << "EOP" << endl;
}

