#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <semaphore.h>

sem_t *semaphore;

void* helloWorld(void* arg);

int main(int argc, char *argv[])
{

    if ((semaphore = sem_open("/semaphore", O_CREAT, 0644, 1)) == SEM_FAILED ) {
        perror("sem_open");
        exit(EXIT_FAILURE);
    }

    // sem_wait(semaphore);
    // sem_post(semaphore);

     pthread_t thdHelloWorld;
     pthread_create(&thdHelloWorld, NULL, helloWorld, NULL);

     while(1) {
         sem_post(semaphore);
         printf("In main, sleep several seconds.\n");
         sleep(1);
     }
     void *threadResult;
     pthread_join(thdHelloWorld, &threadResult);

    if (sem_close(semaphore) == -1) {
        perror("sem_close");
        exit(EXIT_FAILURE);
    }

    if (sem_unlink("/semaphore") == -1) {
        perror("sem_unlink");
        exit(EXIT_FAILURE);
    }

    puts("Done");
    exit(EXIT_SUCCESS);
}

void* helloWorld(void* arg) {
    while(1) {
         // Wait semaphore
         sem_wait(semaphore);
         printf("Hello World\n");
        sleep(1);
     }
}

