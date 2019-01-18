// REF:
// https://pagefault.blog/2018/03/01/common-misconception-with-cpp-move-semantics/
//
// Cppreference.com has this to say about move:
// 
// std::move is used to indicate that an object t may be “moved from”, i.e. allowing the efficient transfer of resources from t to another object.
//
// Moving is especially useful when working with temporary objects, rvalues. Moving can prevent unnecessary copying when temporary objects are passed as parameter or returned.
//
// In particular, std::move produces an xvalue expression that identifies its argument t. It is exactly equivalent to a static_cast to an rvalue reference type.
//
// https://stackoverflow.com/a/37443572
// * move steal things from moved-from obj
// * moved-from obj shouldn't be used any more, or at cautious
// * move only cast to rvalue ref, it's up to the caller to operate on this rvalue ref




#include <iostream>
#include <vector>

using namespace std;

void expr1() {
  cout << "---------expr1 move from local var to local var----------" << endl;
  std::vector<int> a = {1, 2, 3, 4, 5};
  cout << "a: " << &a << endl;
  std::vector<int> b = std::move(a);
  cout << "b: " << &b << endl;

  std::cout << "a: " << a.size() << std::endl;
  std::cout << "b: " << b.size() << std::endl;
  cout << "---------expr1 END----------" << endl;
}

class Data2 {
public:
    Data2(const std::vector<int>& data): m_data(data) {}

    size_t size() const { return m_data.size(); }

private:
    std::vector<int> m_data;
};

void expr2() {
  cout << "---------expr2 [wrong] move from local var to class c'tor----------" << endl;
  std::vector<int> a = {1, 2, 3, 4, 5};

  auto d = Data2(std::move(a));
  std::cout << "a: " << a.size() << std::endl;
  std::cout << "d: " << d.size() << std::endl;
  cout << "---------expr2 END----------" << endl;
}

class Data3 {
public:
    // takes lvalue reference as parameter
    Data3(const std::vector<int>& data): m_data(data) {}

    // takes rvalue reference as parameter
    Data3(std::vector<int>&& data): m_data(std::move(data)) {}

    size_t size() const { return m_data.size(); }

private:
    std::vector<int> m_data;
};

void expr3() {
  cout << "---------expr3 [right] move from local var to class c'tor----------" << endl;
  std::vector<int> a = {1, 2, 3, 4, 5};

  auto d = Data3(std::move(a));
  std::cout << "a: " << a.size() << std::endl;
  std::cout << "d: " << d.size() << std::endl;

  auto c = Data3({1,2,3,4,5});
  std::cout << "c: " << c.size() << std::endl;
  cout << "---------expr3 END----------" << endl;
}

struct BigItem {
  char* data;
};

void expr4() {
  cout << "---------expr4 move from local var to local var----------" << endl;
  std::vector<BigItem> a = {BigItem(), BigItem()};
  for (const auto& item : a) {
    cout << &item << " ";
  }
  cout << endl;
  std::vector<BigItem> b = std::move(a);
  for (const auto& item : b) {
    cout << &item << " ";
  }
  cout << endl;

  std::cout << "a: " << a.size() << std::endl;
  std::cout << "b: " << b.size() << std::endl;
  cout << "---------expr4 END----------" << endl;
}


int main () {
  expr1();
  expr2();
  expr3();
  expr4();

  return 0;
}
