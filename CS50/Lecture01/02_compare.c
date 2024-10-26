#include <stdio.h> 

int main(void)
{
    int x, y;

    printf("Enter value for x: ");
    scanf("%d", &x);

    printf("Enter value for y: ");
    scanf("%d", &y);

    if (x > y)
    {
        printf("X is greater than Y\n");
    }
    else if (x < y)
    {
        printf("X is lower than Y\n");
    }
    else
    {
        printf("X is the same as Y\n");
    }
    return 0;
}
