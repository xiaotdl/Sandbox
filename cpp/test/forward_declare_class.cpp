#include <iostream>

using namespace std;

struct First;           // incomplete declaration of struct First

struct Second {         // complete declaration of struct Second
  Second(First& oneref);
  ~Second() = default;

  // Second() {
  //   // up = std::make_unique<First>();
  //   // cout << up->val << endl; // XXX: error: member access into incomplete type 'First'
  //                               // unless we include First.h in Second.cpp
  // }

  First* oneptr;
  First& oneref;
  // First one;                 // XXX: error: field has incomplete type 'First'
  // std::unique_ptr<First> up; // XXX: error: invalid application of 'sizeof' to an incomplete type 'First'
  std::shared_ptr<First> sp;

  First& f(First& one);
};

Second::Second(First& oneref) : oneref(oneref) {} // Needed. Otherwise XXX: error: constructor for 'Second' must explicitly initialize the reference member 'oneref'

First& Second::f(First& one) {
  return one;
}

struct First {
  int val;
};




// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  cout << "EOP" << endl;
}

