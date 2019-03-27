#include <iostream>

using namespace std;

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  int* ptr = nullptr;
  ptr->non_exist_member;
  cout << *ptr; // >> /bin/bash: line 1:  5944 Segmentation fault: 11  ./a.out
  
}

