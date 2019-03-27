#include <iostream>

using namespace std;

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  cout << 1 << ","
       << ((1 > 2) ? "2" : "NA") << "," 
       << 3
       << endl;
  cout << "EOP" << endl;
  cout << ("123"+std::to_string(4)) << endl;
}

