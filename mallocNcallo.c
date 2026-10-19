#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *ptr1 = (int *)malloc(sizeof(int) * 5);
    int *ptr2 = (int *)calloc(5, sizeof(int));

    // if allocation fail
    if (ptr1 == NULL || ptr2 == NULL )
    {
        printf("Memory allocation failed!\n");
        return 1;
    }

    for (int i = 0; i < 5; i++) {
        printf("pointer 1 address: %p, value: %d\n", (void *)&ptr1[i], ptr1[i]);
        printf("pointer 2 address: %p, value: %d\n", (void *)&ptr2[i], ptr2[i]);
    }

    ptr1[0] = 1993;
    ptr1[4] = 1001;
    ptr2[3] = -225;

    for (int i = 0; i < 5; i++) {
        printf("pointer 1 address: %p, value: %d\n", (void *)&ptr1[i], ptr1[i]);
        printf("pointer 2 address: %p, value: %d\n", (void *)&ptr2[i], ptr2[i]);
    }
    return 0;
}

