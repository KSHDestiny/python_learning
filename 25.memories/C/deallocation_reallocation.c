#include <stdio.h>
#include <stdlib.h>

int main()
{
    int* x;
    x = (int*)malloc(4 * sizeof(int));
    *x = 42;
    printf("Our value: %d\n", *x);

    int *y = x;
    printf("Before update: %d\n", *y);
    *x = 20;
    printf("After update: %d\n", *y);
    free(x);

    // Allocate and free some extra memory blocks
    for (int i = 0; i < 100; i++) {
        int* temp = (int*)malloc(4 * sizeof(int));
        free(temp);
    }

    x = NULL;
    y = NULL;

    int* z = (int *)malloc(4 * sizeof(int));
    *z = 454545;
    printf("After freeing: %d\n", *y);
    return 0;
}
