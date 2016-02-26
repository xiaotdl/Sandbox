// declare:              struct Books *struct_ptr;
// assign addr to ptr:   struct_ptr = &Books1;
// access struct member: struct_ptr->title;

#include <stdio.h>
#include <string.h>

struct Books {
    char title[50];
    char author[50];
    char subject[100];
    int book_id;
};

void printBook( struct Books *book );

int main() {
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

    printBook(&Book1);
    printBook(&Book2);

    return 0;
}

void printBook(struct Books *book) {
    printf("\n");
    printf( "Book title : %s\n", book->title);
    printf( "Book author : %s\n", book->author);
    printf( "Book subject : %s\n", book->subject);
    printf( "Book book_id : %d\n", book->book_id);
} 

