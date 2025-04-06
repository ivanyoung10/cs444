# Project 1: Hello Threads


## Building

Command line:

* `make` to build. An executable called `hellothread` will be produced.
* `make clean` to clean up all build products except the executable.
* `make pristine` to clean up all build products entirely.


## Files


* `hellothread.c`: The file that contains the main code to run the program

## Data


There is a pthread_t array that contains all of the threads for the program.

## Functions

* `main()`
  * `pthread_create()`: Creates the threads for the program
  * `pthread_join()`: Waits for the threads to finish
* `run()`: Argument function for pthread_create(), prints out the thread and number of iteration

## Notes

Should be correct on every run hopefully.
