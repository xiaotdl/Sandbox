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
  cout << &item << endl;
  return item;
}

// Out: Impossible to copy, e.g. unique_ptr
// X f()
unique_ptr<Item> f_out_2() {
  auto item = make_unique<Item>(200);
  cout << item.get() << endl;
  return item;
}

// Out: Cheap/Moderate to move, e.g. vector<T>, string
// X f()
vector<Item> f_out_3() {
  vector<Item> items;
  items.emplace_back(301);
  items.emplace_back(302);
  cout << &items << endl;
  return items;
}

// Out: Expensive to move, e.g. array<BIGPOD>
// f(X&)
void f_out_4(array<BigItem, 10>& bigItems) {
  BigItem bi(4);
  bigItems[0] = bi;
  cout << &bigItems << endl;
}

// --------------------------------------------------
// In/Out
// f(X&)
void f_in_out_1(Item& item) {
  item.val = 1000;
  cout << &item << endl;
}

// --------------------------------------------------
// In/In & Retain "Copy": Cheap to copy, e.g. int
// f(X)
void f_in_1(Item item) {
  cout << &item << endl;
}

// In/In & Retain "Copy": Impossible to copy, e.g. unique_ptr
// f(X)
void f_in_2(unique_ptr<Item> itemUp) {
  cout << itemUp.get() << endl;
  cout << itemUp->val << endl;
}

// In/In & Retain "Copy": Cheap/Moderate/Expensive to move
// f(const X&)
void f_in_3(const vector<Item>& items) {
  cout << &items << endl;
  for (auto& item : items) {
    cout << item.val << endl;
  }
}

int main() {
  // --------------------------------------------------
  // == out ==
  cout << "f_out_1() - X f() - Out: Cheap to copy, e.g. int" << endl;
  auto item1 = f_out_1();
  cout << &item1 << endl;
  cout << item1.val << endl;

  cout << "f_out_2() - X f() - Out: Impossible to copy, e.g. unique_ptr" << endl;
  auto itemUp2 = f_out_2();
  cout << itemUp2.get() << endl;
  cout << itemUp2->val << endl;

  cout << "f_out_3() - X f() - Out: Cheap/Moderate to move, e.g. vector<T>, string" << endl;
  auto items = f_out_3();
  cout << &items << endl;

  cout << "f_out_4() - f(X&) - Out: Expensive to move, e.g. array<BIGPOD>" << endl;
  array<BigItem, 10> bigItems;
  cout << &bigItems << endl;
  f_out_4(bigItems);
  cout << bigItems[0].val << endl;

  // --------------------------------------------------
  // == in/out ==
  cout << "f_in_out_1() - f(X&)" << endl;
  Item item_in_out_1;
  cout << &item_in_out_1 << endl;
  f_in_out_1(item_in_out_1);
  cout << item_in_out_1.val << endl;

  // --------------------------------------------------
  // == in/in & retain "copy" ==
  cout << "f_in_1() - f(X) - In/In & Retain \"Copy\": Cheap to copy, e.g. int" << endl;
  Item item_in_1;
  cout << &item_in_1 << endl;;
  f_in_1(item_in_1);

  cout << "f_in_2() - f(X) - In/In & Retain \"Copy\": Impossible to copy, e.g. unique_ptr" << endl;
  auto itemUp_in_2 = make_unique<Item>(20000);
  cout << itemUp_in_2.get() << endl;
  f_in_2(std::move(itemUp_in_2));
  // cout << itemUp_in_2->val << endl; ==> Segmentation fault

  cout << "f_in_3() - f(const X&) - In/In & Retain \"Copy\": Cheap/Moderate/Expensive to move" << endl;
  vector<Item> items_in_3;
  items_in_3.emplace_back(30001);
  items_in_3.emplace_back(30002);
  cout << &items_in_3 << endl;
  f_in_3(items_in_3);

  cout << "EOP" << endl;
}

