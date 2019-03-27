#include <iostream>

struct X {
    template<class T>
    T good(T n);

    template<class T>
    T bad(T n);

    template<typename K, typename V>
    void record(K k, V v);
};

template<class T>
struct identity { using type = T; };

// OK: equivalent declaration
template<class V>
V X::good(V n) { return n; }

// // Error: not equivalent to any of the declarations inside X
// template<class T>
// T X::bad(typename identity<T>::type n) { return n; }
template<class T>
T X::bad(T n) { return n; }

template<typename K, typename V>
void X::record(K k, V v) {
  std::cout << "recording..." << std::endl;
}

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  X x;
  x.record(1,2);
  std::cout << "EOP" << std::endl;
}

