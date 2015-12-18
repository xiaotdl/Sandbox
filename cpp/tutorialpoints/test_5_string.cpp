#include <iostream>
using namespace std;

int main()
{ 
/* == C++ Strings ==
 * C++ provides 2 types of string representations:
 *  - the C-style character string
 *  - the string class type introduced with Standard C++
 */

/* The C-Style Character String
 * This string is actually a one-dimensional array of characters which 
 * terminates by a null char '\0'.
 * e.g.
 * char greeting[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
 * same as >>>
 * char greeting[] = "Hello";
 * <<<
 *
 * Actually, C++ compiler automatically places the '\0' at the end of
 * the string when it initializes the array.
 */
    char greeting[6] = {'H', 'e', 'l', 'l', 'o', '\0'};

    cout << "Greeting message: ";
    cout << greeting << endl;

/* C++ functions that manipulate null-terminated strings:
 * strcpy(s1, s2)
 * strcat(s1, s2)
 * strlen(s1)
 * strcmp(s1, s2): returns 0 is s1 == s2, <0 if s1 < s2, >0 if s1 > s2
 * strchr(s1, ch): returns a pointer to the first occurrance of char ch in str s1
 * strstr(s1, s2): returns a pointer to the first occurrance of str s2 in str s1
 */
    char str1[10] = "Hello";
    char str2[10] = "World";
    char str3[10];
    int  len;

    // copy str1 into str3
    strcpy(str3, str1);
    cout << "strcpy(str3, str1) : " << str3 << endl;

    // concatenates str1 and str2
    strcat(str1, str2);
    cout << "strcat(str1, str2) : " << str1 << endl;

    // total length of str1 after concatenation
    len = strlen(str1);
    cout << "strlen(str1) : " << len << endl;
// >>>
// strcpy(str3, str1) : Hello
// strcat(str1, str2) : HelloWorld
// strlen(str1) : 10
// /bin/bash: line 1: 24935 Abort trap: 6           ./a.out

// shell returned 134

/* The String Class in C++
 * The standard C++ library provides a string class type that supports
 * all operations mentioned above.
 */
    string s1 = "Hello";
    string s2 = "World";
    string s3;
    int size;

    // copy s1 into s3
    s3 = s1;
    cout << "s3 : " << s3 << endl;

    // concatenates s1 and s2
    s3 = s1 + s2;
    cout << "s1 + s2 : " << s3 << endl;

    // total length of s3 3 3 after concatenation
    size = s3.size();
    cout << "s3.size() : " << size << endl;


    return 0;
}
