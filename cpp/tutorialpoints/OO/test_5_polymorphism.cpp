#include <iostream>
using namespace std;

class Shape {
   protected:
      int width, height;
   public:
      Shape( int a=0, int b=0)
      {
         width = a;
         height = b;
      }

      // without virtual: static resolution of the function call, or static linkage, or early binding
      // with virtual   : dynamic linkage, or late binding
      virtual int area()
      {
         cout << "Parent class area :" <<endl;
         return 0;
      }
      // pure virtual function
      // virtual int area() = 0;
};
class Rectangle: public Shape{
   public:
      Rectangle( int a=0, int b=0):Shape(a, b) { }
      int area ()
      { 
         cout << "Rectangle class area :" <<endl;
         return (width * height); 
      }
};
class Triangle: public Shape{
   public:
      Triangle( int a=0, int b=0):Shape(a, b) { }
      int area ()
      { 
         cout << "Triangle class area :" <<endl;
         return (width * height / 2); 
      }
};

int main()
{ 
/* == Polymorphism in C++ ==
 * Polymorphism meaning having many forms.
 * C++ polymorphism means that a call to a member function
 * will cause a different function to be executed depending on
 * the type of object that invokes the function.
 */
    Shape *shape;
    Rectangle rec(10,7);
    Triangle  tri(10,5);

    // store the address of Rectangle
    shape = &rec;
    // call rectangle area.
    cout << shape->area() << endl;

    // store the address of Triangle
    shape = &tri;
    // call triangle area.
    cout << shape->area() << endl;

    return 0;
}

