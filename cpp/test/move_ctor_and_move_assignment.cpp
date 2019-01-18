#include <iostream>
#include <vector>

#include "MemoryBlock.h"

using namespace std;

template<class T>
void printVector(vector<T>& v) { 
  for (const auto& item : v) {
    cout << &item << " " << item.length() << endl;
  }
}

void expr1() {
  cout << "---------expr1 push_back()----------" << endl;

  vector<MemoryBlock> v;
  v.reserve(256);

  cout << "push_back 25" << endl;
  v.push_back(MemoryBlock(25));
  printVector(v);

  cout << "push_back 75" << endl;
  v.push_back(MemoryBlock(75));
  printVector(v);

  cout << "insert 50" << endl;
  v.insert(v.begin() + 1, MemoryBlock(50));
  printVector(v);
  cout << "---------expr1 END----------" << endl;
}

void expr2() {
  cout << "---------expr2 emplace_back()----------" << endl;

  vector<MemoryBlock> v;
  v.reserve(256);

  cout << "emplace_back 25" << endl;
  v.emplace_back(25);
  printVector(v);

  cout << "emplace_back 75" << endl;
  v.emplace_back(75);
  printVector(v);
  cout << "---------expr2 END----------" << endl;
}

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  expr1();
  expr2();
}

