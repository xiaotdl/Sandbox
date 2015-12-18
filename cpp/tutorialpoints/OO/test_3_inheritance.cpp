#include <iostream>
using namespace std;

// Base class Shape
class Shape {
    public:
        void setWidth(int w) {
            width = w;
        }
        void setHeight(int h) {
            height = h;
        }
    protected:
        int width;
        int height;
};

// Base class PaintCost
class PaintCost {
    public:
        int getCost(int area) {
            return area * 70;
        }
};

// Derived class
class Rectangle: public Shape, public PaintCost {
    public:
        int getArea() {
            return width * height;
        }
};

int main()
{ 
/* == C++ Inheritance ==
 * base class, derived class
 * syntax:
 * class derived-class: access-specifier base-class
 */
    Rectangle Rect;
    int area;
    
    Rect.setWidth(5);
    Rect.setHeight(7);

    area = Rect.getArea();

    // Print the area of the object.
    cout << "Total area: " << Rect.getArea() << endl;


    // Print the total cost of painting
    cout << "Total paint cost: $" << Rect.getCost(area) << endl;


/* Access control and Inheritance
 * A derived class can access all the non-private members of its
 * base class.
 * -----------------------------------------------
 * | Access       | public | protected | private |
 * -----------------------------------------------
 * | Same class   | yes    | yes       | yes     |
 * -----------------------------------------------
 * | Derived class| yes    | yes       | no      |
 * -----------------------------------------------
 * | Outside class| yes    | no        | no      |
 * -----------------------------------------------
 *
 * A derived class inherits all base class methods with the following
 * exceptions:
 *  - Constructors, destructors, and copy constructors of the base class.
 *  - Overloaded operators of the base class.
 *  - The friend functions of the base class.
 */


/* Type of Inheritance
 * The base class can be inherited through public, protected, or private inheritance.
 */


/* Multiple Inheritance
 * syntax:
 * class derived-class: access-specifier baseA, access baseB ...
 */

    return 0;
}

