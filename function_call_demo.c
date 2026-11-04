#include <stdio.h>

void call_by_value(int a, int b) {
    int temp = a;
    a = b,
    b = temp;
}

void call_by_reference(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(void) {
    int num1 = 50, num2 = 100;
    printf("Before swapping, num1 is %d, num2 is %d\n", num1, num2);
    call_by_value(num1, num2);
    printf("Calling function by value...\n");
    printf("After swapping, num1 is %d, num2 is %d\n", num1, num2);

    printf("Calling function by reference...\n");
    call_by_reference(&num1, &num2); // int *a = &num1, int *b = &num2 
    printf("After swapping, num1 is %d, num2 is %d\n", num1, num2);

    return 0;
}