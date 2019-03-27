#include <iostream>

using namespace std;

#define TEST_EQ(a, b)             \
  do {                            \
    bool eq = (a == b);           \
    std::cout << eq << std::endl; \
  } while (false)                 \


// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  TEST_EQ(1, 1);
  TEST_EQ(0, 1);
  cout << "EOP" << endl;
}

