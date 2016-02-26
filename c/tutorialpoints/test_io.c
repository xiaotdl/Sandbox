/* standard files:
 * C programming treats all the devices as files.
 * +---------------+--------------+------------+
 * | Standard File | File Pointer | Device     |
 * +---------------+--------------+------------+
 * |Standard input | stdin        | Keyboard   |
 * +---------------+--------------+------------+
 * |Standard output| stdout       | Screen     |
 * +---------------+--------------+------------+
 * |Standard error | stderr       | Your screen|
 * +---------------+--------------+------------+
 */

// == getchar() ==
// int getchar(void) reads the next available char from the screen n return it as an int

// == putchar() ==
// int putchar(int c) puts the passed char on the screen and returns the same char
// this func puts only single char at a time

// == gets() ==
// char *gets(char *s) reads a line from stdin
// == puts() ==
// int puts(const char *s) writes sting 's' and a trailing newline to stdout

// == scanf() ==
// int scanf(const char *format, ...) reads the input from stream stdin
// and scans that input according to the format provided
// == printf() ==
// int printf(const char *format, ...) writes the output to the stream stdout
// and produces output according to the format provided

// the format can be a simple constant string
// you can specify %s, %d, %c, %f, etc.


#include <stdio.h>

int main() {
    // -----------------------------
    /*int c;*/

    /*printf("\nEnter a value:");*/
    /*c = getchar();*/

    /*printf("\nYou entered:");*/
    /*putchar(c);*/

    // -----------------------------
    char str[100];

    printf("\nEnter a value (format: any):");
    gets(str);

    printf("\nYou entered:");
    puts(str);

    // -----------------------------
    char str1[100];
    int i;

    printf("\nEnter a value (format: %%s %%d):");
    scanf("%s %d", str1, &i);

    printf("\nYou entered: %s %d", str1, i);

    return 0;
}
