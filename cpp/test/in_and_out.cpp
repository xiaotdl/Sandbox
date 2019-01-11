#include <iostream>
#include <vector>
#include <array>

using namespace std;

struct Item {
  Item() = default;
  Item(int val) : val(val) {};

  int val;
};

struct BigItem : public Item {
  using Item::Item;
};

// --------------------------------------------------
// Out: Cheap to copy, e.g. int
// X f()
Item f_out_1() {
  Item item(100);
  return item;
}

// Out: Impossible to copy, e.g. unique_ptr
// X f()
unique_ptr<Item> f_out_2() {
  auto item = make_unique<Item>(200);
  return item;
}

// Out: Cheap/Moderate to move, e.g. vector<T>, string
// X f()
vector<Item> f_out_3() {
  vector<Item> v;
  v.emplace_back(301);
  v.emplace_back(302);
  cout << &v << endl;
  return v;
}

// Out: Expensive to move, e.g. array<BIGPOD>
// f(X&)
void f_out_4(array<BigItem, 10>& bigItems) {
  BigItem bi(4);
  bigItems[0] = bi;
}

// --------------------------------------------------
// In/Out
void f_in_out_1(Item& item) {
  item.val = 1000;
}

// --------------------------------------------------
// In/In & Retain "Copy": Cheap to copy, e.g. int
// f(X)
void f_in_1(int x) {
  cout << x << endl;
}

// In/In & Retain "Copy": Impossible to copy, e.g. unique_ptr
// f(X)
void f_in_2(unique_ptr<Item> itemUp) {
  cout << itemUp->val << endl;
}

// In/In & Retain "Copy": Cheap/Moderate/Expensive to move
// f(const X&)
void f_in_3(const vector<Item>& items) {
  for (auto& item : items) {
    cout << item.val << endl;
  }
}

int main() {
  // --------------------------------------------------
  // == out ==
  auto item1 = f_out_1();
  cout << item1.val << endl;

  auto itemUp2 = f_out_2();
  cout << itemUp2->val << endl;

  auto items = f_out_3();
  cout << &items << endl;

  array<BigItem, 10> bigItems;
  f_out_4(bigItems);
  cout << bigItems[0].val << endl;

  // --------------------------------------------------
  // == in/out ==
  Item item_in_out_1;
  f_in_out_1(item_in_out_1);
  cout << item_in_out_1.val << endl;

  // --------------------------------------------------
  // == in/in & retain "copy" ==
  f_in_1(10000);

  auto itemUp_in_2 = make_unique<Item>(20000);
  f_in_2(std::move(itemUp_in_2));
  // cout << itemUp_in_2->val << endl; ==> Segmentation fault

  vector<Item> items_in_3;
  items_in_3.emplace_back(30001);
  items_in_3.emplace_back(30002);
  f_in_3(items_in_3);

  cout << "EOP" << endl;
}

