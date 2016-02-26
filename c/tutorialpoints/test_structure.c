// == declare structure ==
// struct [structure tag] {
//     member definition;
//     ...
//     member definition;
// } [one or more structure variables];
//
// e.g.
// struct Books {
//     char title[50];
//     char author[50];
//     char subject[100];
//     int  book_id;
// } book;

// == access structure member ==
// member access operater (.)

#include <stdio.h>
#include <string.h>

struct Books {
    char title[50];
    char author[50];
    char subject[50];
    int  book_id;
};

int main() {
    // Declare
    struct Books Book1;
    struct Books Book2;

    // book1, struct member value init
    strcpy( Book1.title, "C Programming" );
    strcpy( Book1.author, "Nuha Ali" );
    strcpy( Book1.subject, "C Programming Tutorial" );
    Book1.book_id = 643897;

    // book2, struct member value init
    strcpy( Book2.title, "Java Programming" );
    strcpy( Book2.author, "Zara Ali" );
    strcpy( Book2.subject, "Java Programming Tutorial" );
    Book2.book_id = 643898;

   /* print Book1 info */
    printf( "Book 1 title : %s\n", Book1.title);
    printf( "Book 1 author : %s\n", Book1.author);
    printf( "Book 1 subject : %s\n", Book1.subject);
    printf( "Book 1 book_id : %d\n\n", Book1.book_id);
 
    /* print Book2 info */
    printf( "Book 2 title : %s\n", Book2.title);
    printf( "Book 2 author : %s\n", Book2.author);
    printf( "Book 2 subject : %s\n", Book2.subject);
    printf( "Book 2 book_id : %d\n", Book2.book_id);
 
    return 0;
}
 

