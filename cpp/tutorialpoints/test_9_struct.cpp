#include <iostream>

using namespace std;
void printBook(struct Books *book);

struct Books {
    char title[50];
    char author[50];
    char subject[100];
    int  book_id;
};

typedef struct {
    char title[50];
    char author[50];
    char subject[100];
    int  book_id;
} YABooks;
// Now define is easier, without using struct keyword:
// Books Book1, Book2;

int main()
{ 
/* == C++ Data Structures==
 */

/* Defining a Structure
 * syntax:
 * struct [structure tag]
 * {
 *    member definition;
 *    member definition;
 *    ...
 *    member definition;
 * } [one or more structure variables];  
 */
    struct Books Book1;        // Declare Book1 of type Books
    struct Books Book2;        // Declare Book2 of type Books

    // Book1 specification
    strcpy( Book1.title, "Learning C++ Programming" );
    strcpy( Book1.author, "Chand Miyan" );
    strcpy( Book1.subject, "C++ Programing" );
    Book1.book_id = 6495407;

   // Book 2 specification
   strcpy( Book2.title, "Telecom Billing");
   strcpy( Book2.author, "Yakit Singha");
   strcpy( Book2.subject, "Telecom");
   Book2.book_id = 6495700;


   // Print Book1 info
   cout << "Book 1 title : " << Book1.title <<endl;
   cout << "Book 1 author : " << Book1.author <<endl;
   cout << "Book 1 subject : " << Book1.subject <<endl;
   cout << "Book 1 id : " << Book1.book_id <<endl;

   // Print Book2 info
   cout << "Book 2 title : " << Book2.title <<endl;
   cout << "Book 2 author : " << Book2.author <<endl;
   cout << "Book 2 subject : " << Book2.subject <<endl;
   cout << "Book 2 id : " << Book2.book_id <<endl;

   cout << endl;

/* Pointers to Structures
 * declare: struct Books *struct_pointer;
 * init:    struct_pointer = &Book1;
 * access:  struct_pointer->title;
 */
   printBook(&Book1);
   printBook(&Book2);


    return 0;
}

void printBook(struct Books *book) {
   cout << "Book title : " << book->title <<endl;
   cout << "Book author : " << book->author <<endl;
   cout << "Book subject : " << book->subject <<endl;
   cout << "Book id : " << book->book_id <<endl;
}
