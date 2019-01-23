#include <iostream>
#include <vector>

using namespace std;

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  vector<int> v;
  cout << &v << endl;

  vector<int>* vPtr = &v;
  cout << vPtr << endl;
  cout << &vPtr << endl;
  cout << "sizeof(vPtr): " << sizeof(vPtr) << endl;

  vector<int>& vRef = v;
  cout << &vRef << endl;
  // cout << &(&vRef) << endl; // ref doesn't have address
  cout << "sizeof(vRef): " << sizeof(vRef) << endl;

  cout << "EOP" << endl;
}

