#include <iostream>
#include <bitset>

using namespace std;

template <class NUM>
void printBits(NUM num) {
  cout << std::bitset<64>(num) << endl;
}

#define GETMASK(index, size) (((1ULL << (size)) - 1) << (index))
#define READFROM(data, index, size) \
  (((data)&GETMASK((index), (size))) >> (index))
#define WRITETO(data, index, size, value)            \
  ((data) = ((data) & (~GETMASK((index), (size)))) | \
       (((uint64_t)value) << (index)))

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  printBits(1ULL);
  cout << endl;

  printBits(-58);
  char a = -58;
  std::bitset<8> x(a);
  cout << x << endl;
  cout << endl;

  int i = 2;
  int size = 3;
  printBits(GETMASK(i, size));
  printBits(~GETMASK(i, size));
  printBits(1ULL << size);
  printBits((1ULL << size) - 1);
  printBits(((1ULL << size) - 1) << i);
  cout << endl;

  uint64_t num = 3ULL;
  WRITETO(num, 0, 0, 4);
  printBits(num);

  cout << "EOP" << endl;
}

