#include <stdio.h>
#include "mythreads.h"
#include <stdlib.h>
#include <pthread.h>

int max;
int i = 0;
int counter = 0; // shared global variable
//volatile int counter = 0; // shared global variable

void *
mythread(void *arg)
{
    char *letter = arg;
    int i; // stack (private per thread)
    printf("%s: begin [addr of i: %p]\n", letter, &i);
    for (i = 0; i < max; i++) {
        counter = counter + 1; // shared: only one
        /*printf("%s: counter=%d\n", letter, counter);*/
    }
    printf("%s: done\n", letter);
    return NULL;
}

int
main(int argc, char *argv[])
{
    /*if (argc != 2) {*/
	/*fprintf(stderr, "usage: main-first <loopcount>\n");*/
	/*exit(1);*/
    /*}*/
    /*max = atoi(argv[1]);*/
    max = 10000;

    pthread_t p1, p2;
    printf("main: begin [counter = %d] [%x]\n", counter,
	   (unsigned int) &counter);
    Pthread_create(&p1, NULL, mythread, "AA");
    Pthread_create(&p2, NULL, mythread, "BB");
    // join waits for the threads to finish
    Pthread_join(p1, NULL);
    Pthread_join(p2, NULL);
    printf("main: done\n [counter: %d]\n [should: %d]\n",
	   counter, max*2);
    return 0;
}

