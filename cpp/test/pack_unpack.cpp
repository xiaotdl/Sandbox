#include <iostream>
#include <string>
#include <bitset>

using namespace std;

// Bits operations
#define GETMASK(index, size) (((1ULL << (size)) - 1) << (index))
#define READFROM(data, index, size) \
  (((data)&GETMASK((index), (size))) >> (index))
#define WRITETO(data, index, size, value)            \
  ((data) = ((data) & (~GETMASK((index), (size)))) | \
       (((uint64_t)value) << (index)))

enum Type : uint8_t {
  A = 0,
  B = 1,
  NUM_OF_TYPES,
};

struct Meta {
  Type type = Type::NUM_OF_TYPES;
  uint64_t numItems = 0;
  uint64_t startByteOffset = 0;

  // debug
  std::string toString() const {
    return std::string(" type: ") + std::to_string(type)
         + std::string(" numItems: ") + std::to_string(numItems)
         + std::string(" startByteOffset: ") + std::to_string(startByteOffset);
  }

  // c'tor
  Meta() {}
  explicit Meta(uint64_t meta) {
    unpack(meta);
  }

  // pack this struct into bits
  // bits layout:
  // |-type(4)-|-numItems(24)-|-startByteOffset(36)-|
  uint64_t pack() const {
    cout << "packing..." << endl;
    uint64_t bits = 0;

    WRITETO(bits, 60, 4, (uint64_t) type);
    cout << std::bitset<64>(bits) << endl;

    WRITETO(bits, 36, 24, numItems);
    cout << std::bitset<64>(bits) << endl;

    WRITETO(bits, 0, 36, startByteOffset);
    cout << std::bitset<64>(bits) << endl;

    return bits;
  }

  // unpack bits into this struct
 void unpack(uint64_t bits) {
    cout << "unpacking..." << endl;
   cout << std::bitset<64>(bits) << endl;
   type = Type(READFROM(bits, 60, 4));
   numItems = READFROM(bits, 36, 24);
   startByteOffset = READFROM(bits, 0, 36);
 }

  // cmp
  bool operator==(const Meta& other) const {
    return type == other.type &&
      numItems == other.numItems &&
      startByteOffset == other.startByteOffset;

  }
};

template<class T>
std::string EQ(T a, T b) {
  return a == b ? "TRUE" : "FALSE";
}

int main() {
  Meta meta1;
  meta1.type = Type::B;
  meta1.numItems = 1;
  meta1.startByteOffset = 1;

  Meta meta2;
  meta2.unpack(meta1.pack());

  cout << "EQ: " << EQ(meta1, meta2) << endl;
  cout << meta1.toString() << endl;
  cout << meta2.toString() << endl;
  cout << "EOP" << endl;
}
