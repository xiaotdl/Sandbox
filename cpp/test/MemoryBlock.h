#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class MemoryBlock {
public:
  // c'tor
  explicit MemoryBlock(size_t length)
    : length_(length)
    , data_(new int[length]) {
      cout << this << " constructor... " << length_ << endl;
  }

  // d'tor
  ~MemoryBlock() {
    cout << this << " destructor.. " << length_ << endl;
    if (data_ != nullptr) {
      cout << this << " \t deleting resource.. " << length_;
      delete[] data_;
      cout << endl;
    }
  }

  // copy c'tor
  MemoryBlock(const MemoryBlock& other)
    : length_(other.length_)
    , data_(new int[other.length_]) {
      cout << this << " copy constructor.. " << other.length_ << "=>" << this->length_ << endl;
      std::copy(other.data_, other.data_ + length_, data_); 
  }

  // copy assignment
  MemoryBlock& operator=(const MemoryBlock& other) {
    cout << this << " copy assignment.. " << other.length_ << "=>" << this->length_ << endl;
    if (this != &other) {
      delete[] data_;
      length_ = other.length_;
      data_ = new int[length_];
      std::copy(other.data_, other.data_ + length_, data_); 
    }
    return *this;
  }

  // move c'tor
  MemoryBlock(MemoryBlock&& other)
    : length_(0)
    , data_(nullptr) {
      cout << this << " move constructor.. " << other.length_ << "=>" << this->length_ << endl;
      // no need to free as we are constructing a new obj

      // copy from other
      length_ = other.length_;
      data_ = other.data_;

      // release other
      other.length_ = 0;
      other.data_ = nullptr;
  }

  // move assignment
  MemoryBlock& operator=(MemoryBlock&& other) {
    cout << this << " move assignment.. " << other.length_ << "=>" << this->length_ << endl;
    if (this != &other) {
      // free this
      delete[] data_;

      // copy from other
      length_ = other.length_;
      data_ = other.data_;

      // release other
      other.length_ = 0;
      other.data_ = nullptr;
    }
    return *this;
  }

  size_t length() const {
    return length_;
  }

private:
  size_t length_; // the length of the resource
  int* data_;     // resource
};
