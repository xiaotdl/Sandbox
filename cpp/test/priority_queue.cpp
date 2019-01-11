#include <iostream>
#include <queue>
#include <functional>

using namespace std;

// -1 if value1 < value2
// 0 if value1 == value2
// 1 if value1 > value2
struct IntLessThanComparator {
   inline bool operator()(const int& x1, const int& x2) {
     return x1 < x2;
  }
};



int main() {
  // auto cmp = [](int x1, int x2) {
  //   return x1 < x2;
  // };
  // std::priority_queue<int, std::vector<int>, decltype(cmp)> heap(cmp);


  using Heap = std::priority_queue<int, std::vector<int>, IntLessThanComparator>;

  std::vector<int> data;
  data.reserve(3);
  Heap heap(IntLessThanComparator(), std::move(data));

  heap.push(5);
  heap.push(2);
  heap.push(4);
  heap.push(3);
  heap.push(3);

  while (!heap.empty()) {
    cout << heap.top() << endl;
    heap.pop();
  }
}
