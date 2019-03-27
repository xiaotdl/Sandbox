#include <iostream>

using namespace std;

#define HELLO(name) \
  std::cout << "'" #name "' Must be non NULL" << std::endl;

#define HELLO2(name) \
  f("'" #name "' Must be non NULL");

void f(std::string msg) {
  std::cout << msg << std::endl;
}

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  HELLO("123");
  HELLO2("123");
  cout << "EOP" << endl;
}

