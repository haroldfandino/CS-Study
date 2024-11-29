#include <stdio.h>
#include <string.h> // For strcmp

int main(void)
{
    // Use char arrays for strings in standard C
    char *strings[] = {"Monica", "Carlos", "Andres", "Jeison", "Eduardo"};
    char *s = "Monica";

    for (int i = 0; i < 5; i++)
    {
        // Use strcmp to compare string contents
        if (strcmp(strings[i], s) == 0)
        {
            printf("Found\n");
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}