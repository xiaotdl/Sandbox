#include <iostream>
#include <vector>

using namespace std;

struct Item {
  Item(int val) : val(val) {}
  int val;
};

class Shop {
public:
  const std::vector<Item>& getItems() const {
    cout << &items_ << endl;
    return items_;
  }
private:
  std::vector<Item> items_;
};

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  Shop shop;
  const auto& items = shop.getItems();
  cout << &items << endl;
  cout << "EOP" << endl;
}

// >>>
// 0x7ffee5c227e8
// 0x7ffee5c227e8
