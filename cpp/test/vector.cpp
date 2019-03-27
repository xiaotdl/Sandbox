#include <iostream>
#include <vector>
#include <string>

using namespace std;

template<class T>
void printVector(std::vector<T> items) {
  for (const auto& item : items) {
    cout << item << ", ";
  }
  cout << endl;
}

class VectorUtil {
  public:
    template<class T>
    static std::string toString(std::vector<T> items) {
      std::string s;
      for (const auto& item : items) {
        s += std::to_string(item) + std::string(", ");
      }
      return s;
    }
};

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  std::vector<int> intVec = {1,2,3};
  printVector(intVec);
  cout << VectorUtil::toString(intVec) << endl;

  std::vector<std::string> strVec = {"hello", "world"};
  printVector(strVec);
  // cout << VectorUtil::toString(strVec) << endl; // only works for numbers

  cout << "EOP" << endl;
}

