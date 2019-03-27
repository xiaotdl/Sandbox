#include <iostream>

#include <bitset>


using namespace std;

template <std::size_t N>
std::bitset<N>
from_string(const std::string& s) {
   return std::bitset<N>(s);
}

template <std::size_t N>
std::string
to_string (const std::bitset<N>& b) {
   return b.template to_string<char,
           std::char_traits<char>,
           std::allocator<char> >();
}



// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  int num = 3432;
  std::bitset<100> b(num);

  // First, bitset provides the usual I/O operators.
  std::cout << "num " <<  num << " in binary is: " << b << endl; 

  // Second, you can convert bitsets to and from strings:
  // there’s a constructor that takes a string argument, and a bitset<>::to_string member function. 
  // You have to write
  //   std::bitset<6>(std::string("110101"));
  // as opposed to just
  //   std::bitset<6>("110101");
  std::cout << std::bitset<8>(std::string("110101")) << endl;
  std::cout << std::bitset<8>(std::string("01010101")).to_ulong() << endl;

  // std::bitset<32> bs;
  // bs.set();
  std::bitset<32>bs(std::string("00000001000000010000000100000001"));
  cout << "bs: " << bs << endl;
  cout << "bs.to_ulong(): " << bs.to_ulong() << endl;

  {
    std::bitset<64>bs(std::string("0000000000000000000000000000000000000000000000000000000000100010"));
    cout << "bs: " << bs << endl;
    cout << "bs.to_ulong(): " << bs.to_ulong() << endl;
  }

  {
    std::bitset<64>bs(std::string("0000000000000000000000000000000000000000000000000000000000000000"));
    cout << "bs: " << bs << endl;
    cout << "bs.to_ulong(): " << bs.to_ulong() << endl;
  }
  
  {
    uint64_t word = 63;
    std::bitset<64>bs(word);
    cout << "bs: " << bs << endl;
    cout << "bs.to_ulong(): " << bs.to_ulong() << endl;
  }

  {
    cout << static_cast<int64_t>(18446744073709551615) << endl;
    cout << static_cast<int64_t>(4323071209347327980) << endl;
  }

  cout << sizeof(unsigned long) << endl;
  cout << "EOP" << endl;
}

