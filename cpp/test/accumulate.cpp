#include <iostream>
#include <vector>
#include <map>
#include <numeric>

using namespace std;

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  {
    vector<int> v = {1,2,3};
    int sum = 0;
    sum = accumulate(v.begin(), v.end(), sum);
    cout << sum << endl;
  }
  {
    map<int, vector<int>> m = {{1,{1,2,3}}, {2,{100,200}}};
    int sum = 0;
    sum = accumulate(m.begin(), m.end(), sum,
        [](const auto& res, const auto& it) { return res + it.second.size(); });
   // for (const auto& kv : m) {
   //   sum += kv.second.size();
   // }
    cout << sum << endl;
  }

  cout << "EOP" << endl;
}

