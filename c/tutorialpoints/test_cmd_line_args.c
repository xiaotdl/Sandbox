// argc: num of args passed
// argv[]: a ptr array which points to each arg passed to the program
// argv[0] - name of the program
// argv[1] - ptr to the first cmd line arg

#include <stdio.h>

int main( int argc, char *argv[] ) {
    printf("argv[0]: %s\n", argv[0]);
    if (argc == 2) {
        printf("The arg supplied is %s\n", argv[1]);
    }
    else if (argc > 2) {
        printf("Too many args.\n");
    }
    else {
        printf("One arg expected.\n");
    }
}

