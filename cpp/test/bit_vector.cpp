// REF:
// Introduction To Bit Vectors
// https://www.youtube.com/watch?v=SYoJ6gUXZvc

#include <iostream>
#include <sstream>
#include <set>
#include <bitset>

#include <stdlib.h>

// BLOCK is a continuous n BYTE of memory.

// * What is the size of the bit vector?
//   BLOCK_SIZE_IN_BITS = sizeof(<block_data_type>) * NUM_BITS_IN_BYTE(=8);
//   NUM_BLOCK = MAX_VALUE/BLOCK_SIZE_IN_BITS + 1
//   bit vector size in bytes = NUM_BLOCK * BLOCK_SIZE_IN_BYTES

// * Where a VALUE will fall into a bit vector?
//   BLOCK_IDX
//       = VALUE / BLOCK_SIZE_IN_BITS
//       = VALUE >> BLOCK_SIZE_LG 
//   BLOCK_INNER_IDX
//       = VALUE % BLOCK_SIZE_IN_BITS
//       = VALUE & BLOCK_MASK 
// * How to set a bit in a bit vector?
//   bit_vector[BLOCK_IDX] |= (1 << BLOCK_INNER_IDX)
//   bit_vector[VALUE / BLOCK_SIZE_IN_BITS] |= (1 << (VALUE % BLOCK_SIZE_IN_BITS))
//   bit_vector[VALUE >> BLOCK_SIZE_LG] |= (1 << (VALUE & BLOCK_MASK))

// * How to test a bit in a bit vector?
//   bit_vector[BLOCK_IDX] & (1 << BLOCK_INNER_IDX)

#define BLOCK_SIZE_IN_BITS 64   // uint64_t
// constexpr int BLOCK_SIZE_IN_BITS = sizeof(uint64_t) * 8;
#define BLOCK_SIZE_IN_BYTES 8   // sizeof(uint64_t)
// constexpr int BLOCK_SIZE_IN_BYTES = sizeof(uint64_t);
#define BLOCK_SIZE_LG 6         // BLOCK_SIZE_LG = log2(BLOCK_SIZE_IN_BITS) = log2(64) = 6
#define BLOCK_MASK 0x3f         // BLOCK_MASK = 0011 1111, set BLOCK_SIZE_LG bits for lower bits, serve as range check


using namespace std;

// void* calloc( std::size_t num, std::size_t size ); 
//   Allocates a contiguous <num> block of memory, with each block <size> bytes.
//   Allocates memory for an array of <num> objects of <size> size and initializes it to all bits zero.
//   If allocation succeeds, returns a pointer to the lowest (first) byte in the allocated memory block that is suitably aligned for any object type.

/*
 * puts 1..maxValue into bit vector, each bit represent one number
 * maps 0..maxValue-1 bits in bit vector 
 */
namespace bitvector {
  int initbv(uint64_t **bv, int maxValue) {
    // int NUM_BLOCK = (maxValue)/BLOCK_SIZE_IN_BITS + 1;
    int NUM_BLOCK = (maxValue + BLOCK_SIZE_IN_BITS - 1)/BLOCK_SIZE_IN_BITS;
	  cout << "init bit vector with NUM_BLOCK: " << NUM_BLOCK << endl;
    *bv = static_cast<uint64_t*>(calloc(NUM_BLOCK, BLOCK_SIZE_IN_BYTES));
    return *bv != NULL;
  }

  void set(uint64_t bv[], int val) {
    int BLOCK_IDX = val >> BLOCK_SIZE_LG;
    int BLOCK_INNER_IDX = val & BLOCK_MASK;
    cout << "Setting val: " << val << ", "
         << "BLOCK_IDX: " << BLOCK_IDX << ", "
         << "BLOCK_INNER_IDX: " << BLOCK_INNER_IDX
         << endl;
    bv[BLOCK_IDX] |= (uint64_t(1) << BLOCK_INNER_IDX);
  }

  bool member(uint64_t bv[], int val) {
    int BLOCK_IDX = val >> BLOCK_SIZE_LG;
    int BLOCK_INNER_IDX = val & BLOCK_MASK;
    cout << "Getting val: " << val << ", "
         << "BLOCK_IDX: " << BLOCK_IDX << ", "
         << "BLOCK_INNER_IDX: " << BLOCK_INNER_IDX
         << endl;
    return (bv[BLOCK_IDX] & (uint64_t(1) << BLOCK_INNER_IDX)) > 0 ? true : false;
  }

	// for debugging use
  // size: BIT_VECTOR_NUM_BLOCK
	string toString(uint64_t bv[], size_t size) {
		stringstream ss;
		for (auto i = 0; i < size; i++) {
			uint64_t word = bv[i];
			// if (word) {
      std::bitset<BLOCK_SIZE_IN_BITS> bs(word);
      ss << "BLOCK"<< i
             << " with bits " << bs << "(" << word << ")"
             << " with bits set at:";
      for (int bit = 0; bit < 64; bit++) {
        if (word & (uint64_t(1) << bit)) {
          ss << " " << i * 64 + bit;
        }
      }
      ss << "\n";
			// }
		}
		return ss.str();
	}

}

void c_style() {
  uint64_t* bv;
  int set1[] = {32, 5, 0};
  int set2[] = {32, 4, 5, 0};
  int maxNum = 32; // max from both sets

  if (!bitvector::initbv(&bv, maxNum)) {
    cout << "calloc failed!" << endl;
    return;
  };

  for (int i = 0; set1[i]; i++) {
    bitvector::set(bv, set1[i]);
  }

  for (int i = 0; set2[i]; i++) {
    if (bitvector::member(bv, set2[i])) {
      cout << set2[i] << endl;
    }
  }

  free(bv);
}

void cpp_style() {
  uint64_t* bv;

  std::set<int> set1 = {100, 63, 11, 5, 1};
  std::set<int> set2 = {100, 63, 11, 4, 5, 2};
  int maxNum = std::max(*set1.rbegin(), *set2.rbegin()); // max from both sets
  cout << "maxNum from both sets: " << maxNum << endl;

  int bitvector_size_in_words = maxNum/BLOCK_SIZE_IN_BITS + 1;

  if (!bitvector::initbv(&bv, maxNum)) {
    cout << "calloc failed!" << endl;
    return;
  };

	cout << "[before set] bitvector::toString():" << endl;
	cout << bitvector::toString(bv, bitvector_size_in_words);
  for (int x : set1) {
    bitvector::set(bv, x);
  }
	cout << "[after set] bitvector::toString():" << endl;
	cout << bitvector::toString(bv, bitvector_size_in_words);

  for (int x : set2) {
    cout << bitvector::member(bv, x) << endl;
  }

  free(bv);
}

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  // cout << "==c_style==" << endl;
  // c_style();

  cout << "==cpp_style==" << endl;
  cpp_style();

  cout << "EOP" << endl;
}

