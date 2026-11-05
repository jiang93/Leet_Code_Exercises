#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>

int count = 0;
int secret_count = 0;

void greet(char *name) {
    printf("Hello %s!\n", name);
}

void goodbye(char *name) {
    printf("Goodbye %s!\n", name);
}

//return_type (*func_ptr_name)(parameter_types)
void synchonous_func_callback(void (*callback_ptr)(char *), char *name) {
    for (int i = 0; i < 3; i++) {
        callback_ptr(name);
    }
}

void show_message(void) {
    printf("Secret count reached!\n");
}

DWORD WINAPI watcher(LPVOID arg) {
    void (*asynchonous_func_callback)(void) = (void (*)(void))arg;

    while (count < secret_count)
    {
        printf("Waiting for secret count...\n");
        Sleep(1);
    }
    asynchonous_func_callback();
    return 0;
}

int main() {
    printf("1. Program started!\n");
    fflush(stdout);

    char user[] = "Hui";
    synchonous_func_callback(greet, user);
    synchonous_func_callback(goodbye, user);

    srand((unsigned int)time(NULL)); // random seed using time
    secret_count = rand() % 20 + 1;
    printf("Secret count is %d\n", secret_count);

    HANDLE hThread = CreateThread(NULL, 0, watcher, (LPVOID)show_message, 0, NULL);

    while(count < secret_count) {
        printf("Current count is %d\n", count);
        count++;
        Sleep(50);
    }

    WaitForSingleObject(hThread, INFINITE);
    CloseHandle(hThread);

    return 0;
}