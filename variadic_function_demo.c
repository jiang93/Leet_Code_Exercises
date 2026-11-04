#include <stdio.h>
#include <stdarg.h>

int sum(int count, ...) {
    va_list args; // declare a variable that tracks the access to additional arguments
    va_start(args, count); // initialize args to start reading the first additional arguments

    int total = 0;
    int value;
    for(int i = 0; i < count; i++) {
        value = va_arg(args, int); // retrieve a new argument
        printf("argument is %d\n", value);
        total += value;
    }
    va_end(args); // required cleanup to match with va_start

    return total;
}

int main(void) {
    
    printf("Sum = %d\n", sum(5, 1, 2, 3, 4, 5));
    printf("Sum = %d\n", sum(5, 10, 20, 30, 40, 50));

    return 0;
}