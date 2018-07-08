#include <stdio.h>
#include "mythreads.h"
#include <stdlib.h>
#include <pthread.h>
#include <string.h>

int x = 0;

void *
mythread(void *arg) {
    // int k = 3;
    // while (k-- > 0) {
    //     printf("%s\n", (char *) arg);
    // }
    if (strcmp(arg, "A") == 0) {
        x += 1;
    }
    if (strcmp(arg, "B") == 0) {
        x += 2;
    }
    printf("%d\n", x);
    return NULL;
}

int
main(int argc, char *argv[])
{
    if (argc != 1) {
        fprintf(stderr, "usage: main\n");
        exit(1);
    }

    pthread_t p1, p2;
    printf("main: begin\n");
    Pthread_create(&p1, NULL, mythread, "A");
    Pthread_create(&p2, NULL, mythread, "B");
    // join waits for the threads to finish
    Pthread_join(p1, NULL);
    Pthread_join(p2, NULL);
    printf("main: end\n");
    return 0;
}

