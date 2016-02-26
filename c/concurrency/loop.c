#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>

char *buffer1;
char *buffer2;
long bufsize;

sem_t *sem_buffer1_empty;
sem_t *sem_buffer1_full;
sem_t *sem_buffer2_empty;
sem_t *sem_buffer2_full;

int *read_from_file_to_buffer1();
int *copy_buffer1_to_buffer2();
int *read_from_buffer2_to_stdout();

int *A() {
    while (1) {
        sem_wait(sem_buffer1_empty);
        printf("Hello from thread A!\n");
        sleep(1);
        /*read_from_file_to_buffer1();*/
        sem_post(sem_buffer1_full);
    }

    return 0;
}

int *B() {
    while (1) {
        sem_wait(sem_buffer1_full);
        sem_wait(sem_buffer2_empty);
        printf("Hello from thread B!\n");
        sleep(1);
        /*copy_buffer1_to_buffer2();*/
        sem_post(sem_buffer1_empty);
        sem_post(sem_buffer2_full);
    }

    return 0;
}

int *C() {
    while (1) {
        sem_wait(sem_buffer2_full);
        printf("Hello from thread C!\n");
        sleep(1);
        /*read_from_buffer2_to_stdout();*/
        sem_post(sem_buffer2_empty);
    }

    return 0;
}

int *read_from_file_to_buffer1() {
    FILE *fp = fopen("file.txt", "r");
    /* Go to the end of the file. */
    fseek(fp, 0L, SEEK_END);

    /* Get the size of the file. */
    bufsize = ftell(fp);

    /* Allocate buffer1 */
    buffer1 = malloc(sizeof(char) * (bufsize + 1));

    /* Go back to the start of the file. */
    fseek(fp, 0L, SEEK_SET);

    /* Read the entire file into memory. */
    fread(buffer1, sizeof(char), bufsize, fp);
    
    fclose(fp);

    return 0;
}

int *copy_buffer1_to_buffer2() {
    /* Allocate buffer2 */
    buffer2 = malloc(sizeof(char) * (bufsize + 1));

    /* copy buffer 1 to buffer2 */
    memcpy(buffer2, buffer1, bufsize);

    free(buffer1);

    return 0;
}

int *read_from_buffer2_to_stdout() {
    /* output buffer2 to stdout */
    fwrite(buffer2, bufsize, 1, stdout);

    free(buffer2);

    return 0;
}

int main() {
    sem_buffer1_empty = sem_open("/sem_buffer1_empty", O_CREAT, 0644, 1);
    sem_buffer1_full = sem_open("/sem_buffer1_full", O_CREAT, 0644, 0);
    sem_buffer2_empty = sem_open("/sem_buffer2_empty", O_CREAT, 0644, 1);
    sem_buffer2_full = sem_open("/sem_buffer2_full", O_CREAT, 0644, 0);

    pthread_t threadA, threadB, threadC;

    pthread_create(&threadA, NULL, (void*) &A, NULL);
    pthread_create(&threadB, NULL, (void*) &B, NULL);
    pthread_create(&threadC, NULL, (void*) &C, NULL);

    pthread_join(threadA, NULL);
    pthread_join(threadB, NULL);
    pthread_join(threadC, NULL);

    sem_close(sem_buffer1_empty);
    sem_close(sem_buffer1_full);
    sem_close(sem_buffer2_empty);
    sem_close(sem_buffer2_full);
    sem_unlink("/sem_buffer1_empty");
    sem_unlink("/sem_buffer1_full");
    sem_unlink("/sem_buffer2_empty");
    sem_unlink("/sem_buffer2_full");

    return 0;
}
