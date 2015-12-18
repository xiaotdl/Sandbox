#include <iostream>
using namespace std;

class Adder{
   public:
      // constructor
      Adder(int i = 0)
      {
        total = i;
      }
      // interface to outside world
      void addNum(int number)
      {
          total += number;
      }
      // interface to outside world
      int getTotal()
      {
          return total;
      };
   private:
      // hidden data from outside world
      int total;
};

int main()
{ 
/* == Data Abstraction in C++ ==
 * Data abstraction refers to, providing only essential information
 * to the outside world and hiding their backgroun details.
 * Data abstraction relies on separation of interface and implementation.
 * In C++, we use classes to define our own abstract data types (ADT).
 */

/* Benefits of Data Abstraction
 *  - Class internals are protected from inadvertent user-level errors
 *  - Class implementation may evolve over time without requiring 
 *    change in user-level code.
 */


/* == Data Encapsulation in C++ ==
 * All C++ programs are composed of the following 2 fundamental elements:
 *  - program statements (code)
 *  - program data
 *
 * Encapsulation binds together the data and functions that manipulate
 * the data, and that keeps both safe from outside interference and misuse.
 * Data encapsulation let to the important OOP concept of data hiding.
 *
 * Data encapsulation: bundling the data and functions
 * Data abstraction  : exposing only the interfaces and hiding implementation details
 *
 * e.g.
 * getters and setters functions in class
 * expose get/set public functions while keep private class members
 */


/* == Interfaces in C++ (Abstract Classes) ==
 * Abstract class (ABC): provide appropriate base class, served only as interface
 * Concrete class: can be used to instantiate objects
 * e.g.
 *    // pure virtual function providing interface framework.
 *       virtual int getArea() = 0;
 */

    Adder a;
    
    a.addNum(10);
    a.addNum(20);
    a.addNum(30);

    cout << "Total " << a.getTotal() <<endl;

    return 0;
}

