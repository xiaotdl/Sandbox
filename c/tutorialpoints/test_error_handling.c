// == perror() ==
// displays the string you pass to it followed by ": " then the errno value
// == strerror() ==
// returns a ptr to the errno value

// always use stderr file stream to output all the errors.

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

extern int errno;

int main() {
    //-----------------------------------------------
    FILE *pf;

    pf = fopen("unexist_file", "rb");
    if (pf == NULL) {
        fprintf(stderr, "value of errno: %d\n", errno);
        perror("Error printed by perror");
        fprintf(stderr, "Error printed by strerror(errno): %s\n", strerror(errno));
    }

    //-----------------------------------------------
    int dividend = 20;
    int divisor = 4;
    int quotient;

    if ( divisor == 0 ) {
        fprintf(stderr, "Division by zero! Exiting...\n");
        exit(EXIT_FAILURE);
    }

    quotient = dividend / divisor;
    fprintf(stderr, "Value of quotient : %d\n", quotient );

    exit(EXIT_SUCCESS);
}
