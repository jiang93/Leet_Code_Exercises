#include <stdio.h>

int factorial(int n);
int binary_search(int *arr, int start_id, int end_id, int target);

int main() {

    int result = factorial(7);
    printf("Factorial result: %d\n", result);
    
    int int_arr[] = {12, 34, 48, 65, 202};
    int search = binary_search(int_arr, 0, 4, 34);
    if (search != -1) {
        printf("Element found: index %d\n", search);
    }
    else {
        printf("Element not found\n");
    }
    
    return 0;
}

int factorial(int n){
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n-1); 
}

int binary_search(int *arr, int start_id, int end_id, int target) {
    
    if (start_id > end_id) {
        return -1;
    }
    int mid_id = (start_id + end_id)/2;
    //printf("middle index: %d\n", mid_id);
    
    if (arr[mid_id] == target) {
        return mid_id;
    }
    else if (target < arr[mid_id]) {
        return binary_search(arr, start_id, mid_id-1, target);
    }
    else {
        return binary_search(arr, mid_id+1, end_id, target);
    }
}