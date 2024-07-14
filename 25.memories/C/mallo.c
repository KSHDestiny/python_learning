#include <stdio.h>
#include <stdlib.h>

int main()
{
    int* x;
    x = (int *)malloc(4 * sizeof(int));
    *x = 42;
    printf("Our value: %d\n", *x);

    int *y = x;
    printf("Before update: %d\n", *y);
    *x = 20;
    printf("After update: %d\n", *y);
    return 0;
}