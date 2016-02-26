#include <stdio.h>

int count;
extern void write_extern();

int main() {
    count = 5;
    write_extern();
}

// >>>
// ➜  tutorialpoints $ gcc test_extern_main.c test_extern_support.c
// ➜  tutorialpoints $ ./a.out
// count is 5
