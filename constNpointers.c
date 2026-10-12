#include <stdio.h>

int main(void)
{
    // const variable
    const int a = 10; // a = 20; error
    printf("Value of a: %d\n", a);

    // pointer to const variable
    const int b = 20;
    const int c = 30;
    const int *p = &b; // *p = 25; error

    printf("Address that p is pointing to: %p\n", (void*)p);
    printf("Value that p is pointing to: %d\n", *p);
    
    p = &c; // pointer can point elsewhere
    printf("Address that p is pointing to: %p\n", (void*)p);
    printf("Value that p is pointing to: %d\n", *p);

    // const pointer to a variable
    int d = 40;
    int e = 50;
    int *const ptr = &d; // ptr = &e; error

    printf("Address that ptr is pointing to: %p\n", (void*)ptr);
    printf("Value that ptr is pointing to: %d\n", *ptr);

    *ptr = 45;

    printf("Address that ptr is pointing to: %p\n", (void*)ptr);
    printf("Value that ptr is pointing to: %d\n", *ptr);
    printf("Address of d: %p\n", (void*)&d);
    printf("Value of d: %d\n", d);

    // const pointer to a const variable
    const int x = 60;
    const int y = 70;
    const int *const pointer = &x;

    // *pointer = 65; error
    // pointer = &y; error 

    printf("Address that pointer is pointing to: %p\n", (void*)pointer);
    printf("Value that pointer is pointing to: %d\n", *pointer);

}