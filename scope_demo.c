#include <stdio.h>

void count() {
    auto int a = 0; // auto create and initialize variable to 0 every entry
    static int b = 0; // initialize to 0, and preserves variable value until program ends

    a++;
    b++;

    printf("a is %d, b is %d\n", a, b);
}

int main() {
    count();
    count();
    count();

    return 0;
}