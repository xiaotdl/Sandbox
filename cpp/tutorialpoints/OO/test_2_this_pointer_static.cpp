#include <iostream>
using namespace std;

class Box {
    public:
        static int objectCount;
        Box(double l=2.0, double b=2.0, double h=2.0) {
            cout << "Contructor called." << endl;
            length = l;
            breadth = b;
            height = h;
            objectCount++;
        }
        double Volume() {
            return length * breadth * height;
        }
        int compare(Box box) {
            return this->Volume() > box.Volume();
        }
        static int getCount() {
            return objectCount;
        }
    private:
        double length;
        double breadth;
        double height;
};

int Box::objectCount = 0;

int main()
{ 
/* == C++ this pointer == */
    Box Box1(3.3, 1.2, 1.5);    // Declare box1
    Box Box2(8.5, 6.0, 2.0);    // Declare box2

    if(Box1.compare(Box2))
    {
       cout << "Box2 is smaller than Box1" <<endl;
    }
    else
    {
       cout << "Box2 is equal to or larger than Box1" <<endl;
    }

    Box *ptrBox;                // Declare pointer to a class.

    ptrBox = &Box1;             // Save the address of the first object
    cout << "Volume of Box1: " << ptrBox->Volume() << endl; // access member

    ptrBox = &Box2;             // Save the address of the first object
    cout << "Volume of Box2: " << ptrBox->Volume() << endl; // access member

/* == Static member of a C++ class ==
 * static member is shared by all objects of the class.
 * All static data is initialized to zero when the first object is created.
 */
    // Print total number of objects.
    cout << "Total objects: " << Box::objectCount << endl;

/* Static Function Member */
    cout << "Final Stage Count: " << Box::getCount() << endl;

    return 0;
}
