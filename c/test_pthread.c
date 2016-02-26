#include <stdio.h>
#include <unistd.h>
#include <pthread.h>


void* tprocess1(void* args){
         while(1){
                 printf( "tprocess1...\n");
                 fflush(stdout);
                 sleep(1);
         }
         return NULL;
}

void* tprocess2(void* args){
         while(1){
                 printf("tprocess2...\n");
                 fflush(stdout);
                 sleep(1);
         }
         return NULL;
}

int main(){
         pthread_t t1;
         pthread_t t2;
         pthread_create(&t1,NULL,tprocess1,NULL);
         pthread_create(&t2,NULL,tprocess2,NULL);
         pthread_join(t1,NULL);
         return 0;
}
