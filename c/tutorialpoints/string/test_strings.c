// strings:
// one-dimensional array of chars terminated by a null char '\0'

// declare and init:
// char greeting[6] = {'H', 'e', 'l', 'l', 'o', '\0'}; // '\0' will be put at the end automatically
// same as >>>
// char greeting[] = "Hello";
// <<<

#include <stdio.h>
#include <string.h>

int main() {
    // same as >>>
    /*char greeting[6] = {'H', 'e', 'l', 'l', 'o', '\0'};*/
    /*char greeting[6] = {'H', 'e', 'l', 'l', 'o'};*/
    char greeting[] = "Hello";
    // <<<

    printf("greeting message: %s\n", greeting);

    // ---------- str methond ----------------
    // strcpy(s1, s2)
    // strcat(s1, s2)
    // strlen(s1)
    // strcmp(s1, s2)
    // strchr(s1, ch)
    // strstr(s1, s2)
    // ...
    char str1[12] = "Hello";
    char str2[12] = "World";
    char str3[12];
    int len;

    /* copy str1 into str3 */
    strcpy(str3, str1);
    printf("strcat(str1, str3): %s\n", str3);

    /* concatenates str1 and str2 */
    strcat(str1, str2);
    printf("strcat(str1, str2): %s\n", str1);

    /* total length of str1 after concatenation */
    len = strlen(str1);
    printf("strlen(str1): %d\n", len);
    len = sizeof(str1);
    printf("sizeof(str1): %d\n", len);

    return 0;
}
