#include <iostream>

using namespace std;

// REF: https://stackoverflow.com/questions/1549930/c-equivalent-of-javas-tostring

// class Person {
//  public:
//   string name;
//   int age;
// };
// 
// std::ostream& operator<<(std::ostream& stream, const Person& person) {
//   return stream << "Person(" << person.name << ", " << person.age << ")";
// }

// In case your operator<< wants to print out internals of class A and really needs access to its private and protected members you could also declare it as a friend function:
class Person {
public:
  Person(string name, int age) : name_(name), age_(age) {}
private:
  friend std::ostream& operator<<(std::ostream&, const Person&);
  string name_;
  int age_;
};

std::ostream& operator<<(std::ostream& stream, const Person& person) {
  return stream << "Person(" << person.name_ << ", " << person.age_ << ")";
}

// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  cout << Person({"Xiaotian", 30}) << endl;
  cout << "EOP" << endl;
}

