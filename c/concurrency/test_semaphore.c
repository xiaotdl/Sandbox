#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>
sem_t mutex;

void *my_thread(void *args) {
    int id = (int)args;
    while(1){
        sem_wait(&mutex);
        printf("Hello from da thread %d!\n", id);
        sem_post(&mutex);
        sleep(1);        
    }
}

int main() {
    int id1=1, id2=2;
    pthread_t thread1_id, thread2_id;
    sem_init(&mutex, 0, 1);
    pthread_create(&thread1_id, NULL, my_thread, (void* )id1);
    pthread_create(&thread2_id, NULL, my_thread, (void* )id2);
    pthread_join(thread1_id, NULL);
    pthread_join(thread2_id, NULL);
    sem_destroy(&mutex);
}

