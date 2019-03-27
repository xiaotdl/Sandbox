#include <iostream>

using namespace std;

enum class Type {
  A=1,
  B=2,
};

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  int x = 1;
  cout << std::to_string(x) << endl;
  // cout << Type::B << endl; // error: invalid operands to binary expression ('std::__1::ostream' (aka 'basic_ostream<char>') and 'Type')
  // cout << std::to_string(Type::B) << endl; // error: no matching function for call to 'to_string'
  cout << int(Type::B) << endl;
  cout << (int)Type::B << endl;
}

