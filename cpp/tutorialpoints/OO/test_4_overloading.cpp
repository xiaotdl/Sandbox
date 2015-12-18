#include <iostream>
using namespace std;

class PrintData {
    public:
        void print(int i) {
            cout << "Printing int  : " << i << endl;
        }
        void print(double f) {
            cout << "Printing fload: " << f << endl;
        }
        void print (char* c) {
            cout << "Printing char : " << c << endl;
        }
};


class Box {
    public:
        double getVolume(void) {
            return length * breadth * height;
        }
        void setLength(double len) {
            length = len;
        }
        void setBreadth(double bre) {
            breadth = bre;
        }
        void setHeight(double hei) {
            height = hei;
        }

        // Overlaod + operator to add two Box objects
        Box operator+(const Box &b) {
            Box box;
            box.length = this->length + b.length;
            box.breadth = this->breadth + b.breadth;
            box.height = this->height + b.height;
            return box;
        }
    private:
        double length;
        double breadth;
        double height;
};

int main()
{ 
/* == C++ Overloading (Operator and Function)==
 * C++ allows you to specify more than one difinition for a function name
 * (function overloading) or an operator (operator overloading) in the same scope,
 * except that both declarations have different arguments and obviously
 * different definition (implementation).
 *
 * The process for compiler to select most appropriate overloaded function
 * or operator is called overload resolution.
 */

/* Function overloading in C++ */
    PrintData pd;

    pd.print(5);
    pd.print(500.263);
    pd.print("Hello C++");

/* Operator overloading in C++
 * You can redefine or overload most of the built-in operators availabe in C++.
 * e.g.
 * Box opperator+(const Box&);
 * Box opperator+(const Box&, const Box&);
 */
    Box Box1;
    Box Box2;
    Box Box3;
    double volume = 0.0;
    
    // box 1 specification
    Box1.setLength(6.0); 
    Box1.setBreadth(7.0); 
    Box1.setHeight(5.0);
 
    // box 2 specification
    Box2.setLength(12.0); 
    Box2.setBreadth(13.0); 
    Box2.setHeight(10.0);

    // volume of box 1
    volume = Box1.getVolume();
    cout << "Volume of Box1 : " << volume <<endl;
 
    // volume of box 2
    volume = Box2.getVolume();
    cout << "Volume of Box2 : " << volume <<endl;

    // Add two object as follows:
    Box3 = Box1 + Box2;

    // volume of box 3
    volume = Box3.getVolume();
    cout << "Volume of Box3 : " << volume <<endl;

    return 0;
}

