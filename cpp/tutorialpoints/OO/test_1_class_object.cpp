#include <iostream>
using namespace std;

/* C++ Class Definition */
class Box {
    public:
        double length;
        double breadth;
        double height;

        double getVolume(void) {
            return length * breadth * height;

        }

        void setLength( double len  );
        void setBreadth( double bre  );
        void setHeight( double hei  );

    protected:
        double var;
};

void Box::setLength( double len )
{
    length = len;
}

void Box::setBreadth( double bre )
{
    breadth = bre;
}

void Box::setHeight( double hei )
{
    height = hei;
}


class ChildBox:Box {
    public:
        double getVar( void );
        void setVar( double v );
};

double ChildBox::getVar(void)
{
    return var;
}
 
void ChildBox::setVar( double v )
{
    var = v;
}


class Line
{
    public:
        double length;
        void setLength( double len );
        double getLength( void );
        Line(double len);  // This is the constructor
        Line(const Line &obj);  // copy constructor
        ~Line();  // This is the destructor
    private:
        double *ptr;
};

// class constructor
Line::Line( double len )
{
    cout << "Object is being created, length = " << len << endl;
    length = len;

    cout << "Normal constructor allocating ptr" << endl;
    // allocate memory for the pointer;
    ptr = new double;
    *ptr = len;
}

// copy constructor
Line::Line(const Line &obj)
{
    cout << "Copy constructor allocating ptr." << endl;
    ptr = new double;
   *ptr = *obj.ptr; // copy the value
}
 
// class destructor
Line::~Line(void)
{
    cout << "Object is being deleted" << endl;

    cout << "Freeing memory!" << endl;
    delete ptr;
}

// Member functions definitions
double Line::getLength(void)
{
    return length ;
}
 
void Line::setLength( double len )
{
    length = len;
}

void display(Line obj) {
    cout << "Length of line : " << obj.getLength() <<endl;
}



int main()
{ 
/* == C++ Classes and Objects ==
 * - Definition
 * - Declare
 */
     Box Box1;  // Declare Box1 of type Box
     Box Box2;  // Declare Box2 of type Box
     double volume = 0.0; 

     // box1 specification
     Box1.height = 5.0;
     Box1.length = 6.0;
     Box1.breadth = 7.0;


     // box 2 specification
     Box2.height = 10.0;
     Box2.length = 12.0;
     Box2.breadth = 13.0;

     // volume of Box1
     volume = Box1.height * Box1.length * Box1.breadth;
     cout << "Volume of Box1 : " << volume <<endl;

     // volume of box 2
     volume = Box2.height * Box2.length * Box2.breadth;
     cout << "Volume of Box2 : " << volume <<endl;

/* C++ class member function */
     Box myBox;
     myBox.getVolume();

     // myBox specification
     myBox.setLength(6.0); 
     myBox.setBreadth(7.0); 
     myBox.setHeight(5.0);

     // volume of myBox
     volume = myBox.getVolume();
     cout << "Volume of myBox : " << volume <<endl;

/* C++ class access modifiers
 * - public    : accessible from anywhere outside the classa but within a program.
 * - private   : not accessible or viewd outside of the class, only the class and
 *               friend functions can access private members. By default, class members
 *               are private members.
 * - protected : similar to a private member but can be accessed in child classes (derived classes).
 *   e.g.
 *   class Base {
 *       public:
 *       protected:
 *       private:
 *   }
 */
     Line line(20.0);

     // set line length
     line.setLength(6.0); 
     cout << "Length of line : " << line.getLength() <<endl;
 
     // set line length without member function
     line.length = 10.0; // OK: because length is public
     cout << "Length of line : " << line.length <<endl;


     ChildBox box;
     box.setVar( 123 );
     cout << "Var of box : "<< box.getVar() << endl;
     cout << endl;

/* Class Constructor */
/* Class Destructor */

// This is a bit confusing!
/* == C++ Copy Constructor ==
 * - initialize one object from another of the same type
 * - copy an object to pass it as an argument to a function
 * - copy an object to return it from a function
 * syntax:
 * classname (const classname &obj) {
 *     // body of constructor
 * }
 */
     Line line1(10); 
     display(line1);
     //>>>
     //    Object is being created, length = 10
     //    Normal constructor allocating ptr
     //    Copy constructor allocating ptr.
     //    Length of line : 0
     //    Object is being deleted
     //    Freeing memory!
     //    Object is being deleted
     //    Freeing memory!


/* == C++ Friend Functions ==
 * A friend function of a class is defined ouside the class's scope but
 * it has the right to access all private and protected members of the class.
 *
 * A friend can be a function, function template, or member function, or a
 * class or class template, in which case the entire class and all of its members
 * are friends.
 *
 * To declare a function as a friend of a class:
 * class Box {
 * public:
 *      friend void printWidth ( Box box );
 * };
 *
 * To declare all member functions of ClassTwo as friends of class ClassOne.
 * friend class ClassTwo;
 */

     return 0;
}
