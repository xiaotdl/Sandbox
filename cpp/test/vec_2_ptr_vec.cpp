#include <iostream>
#include <vector>

using namespace std;


// --------------------------------------------------------------------------------
// vector<T*>& /*in*/, vector<T>& /*out*/
template <typename T>
void getVecFromPtrVec(const std::vector<T*>& src, std::vector<T>& dst) {
  dst.reserve(src.size());
  dst.clear();
  for (int i = 0; i < src.size(); i++) {
    dst.emplace_back(std::move(*src[i]));
  }
}

// vector<T*>& ==> vector<T>&
template <typename T>
vector<T> getVecFromPtrVec(const std::vector<T*>& src) {
  vector<T> dst;
  getVecFromPtrVec(src, dst);
  return dst;
}

// --------------------------------------------------------------------------------
// vector<T>& /*in*/, vector<T*>& /*out*/
template <typename T>
void getPtrVecFromVec(std::vector<T>& src, std::vector<T*>& dst) {
  dst.reserve(src.size());
  for (int i = 0; i < src.size(); i++) {
    dst.push_back(&src[i]);
  }
}

// vector<T>& ==> vector<T*>&
template <typename T>
vector<T*> getPtrVecFromVec(std::vector<T>& src) {
  vector<T*> dst;
  getPtrVecFromVec(src, dst);
  return dst;
}

struct Item {
  Item(int val)
  : val(val) {}

  int val;
};

int main() {
  // ptrVec ==> vec
  Item i1(100);
  Item i2(200);
  vector<Item*> ptrVecA = {&i1, &i2};

  // v1:
  vector<Item> vecB;
  getVecFromPtrVec(ptrVecA, vecB);
  for (const Item& i : vecB) {
    cout << i.val << endl;
  }

  // v2:
  vector<Item> vecC = getVecFromPtrVec(ptrVecA);
  for (const Item& i : vecC) {
    cout << i.val << endl;
  }

  // vec ==> ptrVec
  vector<Item> vecA;
  vecA.emplace_back(300);
  vecA.emplace_back(400);

  // v1:
  vector<Item*> ptrVecB;
  getPtrVecFromVec(vecA, ptrVecB);
  for (const Item* i : ptrVecB) {
    cout << i->val << endl;
  }

  // v2:
  vector<Item*> ptrVecC = getPtrVecFromVec(vecA);
  for (const Item* i : ptrVecC) {
    cout << i->val << endl;
  }
  
  cout << "EOP" << endl;
}

