#include <stdio.h>

int main(void) {

    int count = 1;

    first:
        printf("Welcome!\n");
    
    second:
        printf("Let's start counting!\n");

    start:
        printf("Count: %d\n", count);
        if (count == 3) {
            goto end;
        }
    
    ++count;
    goto start;

    end:
        printf("Finished counting!\n");
}