#include <stdio.h>

// global variables 
int counter_one = 10; 
int counter_two = 20;


static int counter_three = 30; // without static => 'counter_three': redefinition; multiple initialization
extern int counter_four;

void show_data_count(void);

int show_count(void){
    printf("counter_one in show_count function is %d\n", counter_one);
    printf("counter_two in show_count function is %d\n", counter_two);

    return 0;
}

int increment_count(void){
    static int counter_five = 0;
    counter_five ++;
    printf("counter_five is %d\n", counter_five);

}

int main(void)
{
    // check original variables
    show_count();

    int counter_one = 99; // new local variable
    counter_two = 99; // update global variable

    printf("counter_one in main function is %d\n", counter_one);
    printf("counter_two in main function is %d\n", counter_two);

    // check if variables are updated by previous steps
    show_count();

    // check variables in linkage_data.c file
    show_data_count();

    // update and check variables in linkage_demo.c file
    counter_four = 99;
    printf("counter_three in linkage_demo file is %d\n", counter_three);
    printf("counter_four in linkage_demo file is %d\n", counter_four);

    // check variables in linkage_data.c file
    show_data_count();

    increment_count();
    increment_count();
    increment_count();
    
    return 0;
}