#include <stdio.h>

// global variables 
static int counter_three = 35; 
int counter_four = 45;
//int counter_five = 55;

void show_data_count(void)
{
    printf("counter_three in linkage_data file is %d\n", counter_three);
    printf("counter_four in linkage_data file is %d\n", counter_four);
    //printf("counter_five in linkage_data file is %d\n", counter_five);

}