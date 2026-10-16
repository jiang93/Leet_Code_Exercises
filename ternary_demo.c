#include <stdio.h>

int main(void) {

    // ternary syntax for if-esle => condition ? if_value_true : if value_fasle
    /* ternary syntax for if-else if-else => condition1 ? if_value_true 
                                             : condition2 ? if_value_true 
                                             : if_value_false; */
    /* tenary syntax for nested if-else => condition1 ? condition2 ? if_value_true : if_value_false
                                           : condition3 ? if_value_true : if_value_false */
    
    printf("size of secret number is %zu bytes\n", sizeof(int));

    int numOne = 99;
    int numTwo = 45;
    int numThree = 165;

    numOne > 100 ? printf("secret number is greater than 100\n") : printf("secret number is smaller than 100\n");

    numTwo > 100 ? printf("secret number is greater than 100\n")
    : (numTwo > 50 ? printf("secret number is greater than 50\n") 
    : printf("secret number is smaller than 50\n"));

    numThree > 100 ? numThree > 200 ? printf("secret number is greater than 200\n") : printf("secret number is greater than 100 and less than 200\n")
    : numThree > 50 ? printf ("secret number is smaller than 100 and greater than 50\n") : printf("secret number is smaller than 50\n");
    
    return 0;
}