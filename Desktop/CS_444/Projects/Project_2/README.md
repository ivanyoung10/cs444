# Project 2: Mutexes


## Building

Command line:

* `make` to build. An executable called `reservations` will be produced.
* `make clean` to clean up all build products except the executable.
* `make pristine` to clean up all build products entirely.


## Files


* `reservations.c`: The file that contains the main code to run the program

## Data


There is a int array for the number of seats that are reserved, a couple integer variables for seat_count, broker_count, and transaction_count for the user to input. There is also a mutex lock to protect the shared resources.

## Functions

* `reserve_seat()`: reserves a seat if available
* `free_seat()`: frees a seat if it is reserved
* `is_free()`: checks if a seat is free
* `verify_seat_count()`: checks to see if the global variable seat_count reserved seats matches seat_taken_count

## Notes

Works for any number of brokers, and broker transactions, but may slow down your system if both of these numbers are large.
