#include <iostream>
#include <vector>

using namespace std;

struct C {};

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  {
    auto up = make_unique<C>();
    cout << "up.get(): " << up.get() << endl;
    vector<unique_ptr<C>> v;
    // v.push_back(up); // error: call to implicitly-deleted copy constructor of 'std::__1::unique_ptr<C, std::__1::default_delete<C> >'
    v.push_back(std::move(up));
    cout << "v[0].get(): " << v[0].get() << endl;
  }

  {
    vector<unique_ptr<C>> v;
    v.push_back(make_unique<C>());
  }
  cout << "EOP" << endl;
}

