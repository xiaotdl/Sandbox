#include <iostream>
#include <cstring>

using namespace std;

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  // memset works on bytes, so it fills your array of ints with 0x01010101 values (assuming int is 32 bits) which is decimal 16843009.
  int32_t a[10];
  //int64_t a[10];
  cout << sizeof(a) << endl;
  std::memset(a , 1, sizeof(a));
  for (auto x : a) {
    cout << x << endl;
  }
  cout << "EOP" << endl;
}

