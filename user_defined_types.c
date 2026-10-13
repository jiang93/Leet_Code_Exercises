#include <stdio.h>

int main(void) {

    // User-defined Status type
    enum Status {ON, OFF, ERROR};
    enum Status current_status = ON;
    printf("Current status is %d\n", current_status);

    // struct 
    struct Student
    {
        int admin_no;
        char name[20];
    };

    struct Student s1 = {20061, "Hui"}; // struct Student s1 = {.admin_no = 20061, .name = "Hui"};
    printf("Admin number: %d, Name: %s\n", s1.admin_no, s1.name);

    struct Student s2;
    s2.admin_no = 20062;
    strcpy(s2.name, "Gary");
    // s2.gender = "male"; error: struct "Student" has no field "gender"

    printf("Admin number: %d, Name: %s\n", s2.admin_no, s2.name);

    // union
    union Sensor
    {
        int presence;
        int velocity;
        int temperature;
    };

    union Sensor data = {.presence = 1, .velocity = 25, .temperature = 31};
    // presence, velocit and temperature share same memory, only 31 is retained
    printf("Sensor data: %d, %d, %d\n", data.presence, data.velocity, data.temperature);

    return 0;
}