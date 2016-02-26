// dynamic memory mgmt in C
// C provides several functions for memory allocation and mgmt, defined in <stdlib.h>
// == void *calloc(int num, int size) ==
// allocates an array of num elements, each of which in bytes will be size
//
// == void free(void *address) ==
// releases a block of memory
//
// == void *malloc(int num) ==
// allocates an array of num bytes and leave them initialized
//
// == void *realloc(void *address, int newsize) ==
// re-allocates memory extending it upto newsize

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char name[100];
    char *description;

    strcpy(name, "Zara Ali");

    /* allocate memory dynamically */
    description = malloc(30 * sizeof(char));
    if (description == NULL) {
        fprintf(stderr, "Error - unable to allocate required memory\n");
    }

    strcpy(description, "Zara Ali is a DPS student.");

    printf("Name = %s\n", name);
    printf("Description = %s\n", description);
    
    /* suppose you want to store bigger description */
    description = realloc(description, 100 * sizeof(char));
    if (description == NULL) {
        fprintf(stderr, "Error - unable to allocate required memory\n");
    }

    strcat(description, "She is in class 10th.");

    printf("Name = %s\n", name);
    printf("Description = %s\n", description);

    /* release memory using free() function */
    free(description);
}
