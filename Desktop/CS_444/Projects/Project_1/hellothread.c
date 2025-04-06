#include <pthread.h>
#include <stdio.h>

#define NUM_THREADS 2
#define NUM_INTEGERS 5

void *run(void *arg){

    for (int i = 0; i < NUM_INTEGERS; i++){
        printf("thread %d: %d\n", *(int *)arg + 1, i);
    }

    return NULL;
}

int main(void){

    printf("Launching threads\n");

    pthread_t thread_id[NUM_THREADS];

    for (int i = 0; i < NUM_THREADS; i++){
        pthread_create(&thread_id[i], NULL, run, &i);
        pthread_join(thread_id[i], NULL);
    }

    printf("Threads completed!\n");
}
