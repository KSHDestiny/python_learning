#include <stdio.h>
#include <stdlib.h>

int main()
{
    while(1){
        int *x;
        x = (int *)malloc(200000 * sizeof(int));
        if(x == NULL){
            break;
        }
    }
    return 0;
}