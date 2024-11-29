#include <stdio.h>

int main (void)
{
    int numbers[] = {1,2,3,4,50};
    int n = 50;

    for (int i = 0; i < 5; i++)
    {
        if (numbers[i] == n)
        {
            printf("Found\n");
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}