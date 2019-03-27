#include <iostream>

using namespace std;

struct Settings {};
struct Stats {};

struct Context {
  Context(Settings settings)
    : settings(settings) {}

  const Settings settings;
  Stats stats;
};

enum class AnimalType {
  CAT,
  DOG,
};

class Animal {
public:
  explicit Animal(std::shared_ptr<Context> ctx)
    : ctx(std::move(ctx)) {}

  virtual void speak() {
    cout << "I'm a " << getType() << "!" << endl;
  }

  // c++ doesn't have virtual member, use virtual function instead
  // https://stackoverflow.com/questions/3248255/why-doesnt-c-have-virtual-variables
  virtual std::string getType() {
    return type;
  }

private:
  std::string type = "animal";
  std::shared_ptr<Context> ctx;
};

struct Cat : public Animal {
public:
  Cat(std::shared_ptr<Context> ctx)
    : Animal(ctx) {}

  std::string getType() {
    return type;
  }
  
private:
  std::string type = "cat";
};

struct Dog : public Animal {
public:
  Dog(std::shared_ptr<Context> ctx)
    : Animal(ctx) {}

  std::string getType() {
    return type;
  }
  
private:
  std::string type = "dog";
};

class AnimalFactory {
public:
  static unique_ptr<Animal> get(AnimalType type) {
    Settings settings;
    shared_ptr<Context> ctx = make_shared<Context>(settings);
    switch(type) {
      case AnimalType::CAT: 
        return make_unique<Cat>(std::move(ctx));
      case AnimalType::DOG: 
        return make_unique<Dog>(std::move(ctx));
    }
  }
};


// To Run: !g++ -std=c++14 -Wall % && ./a.out
int main() {
  {
    // cat
    unique_ptr<Animal> animal = AnimalFactory::get(AnimalType::CAT);
    animal->speak();
  }

  {
    // dog
    unique_ptr<Animal> animal = AnimalFactory::get(AnimalType::DOG);
    animal->speak();
  }

  cout << "EOP" << endl;
}

