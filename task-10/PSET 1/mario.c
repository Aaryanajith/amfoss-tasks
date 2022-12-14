#include<stdio.h>

int main(void)
{

    int n;
    while(true)
    {
        n=get_int("width :");
        if (n>0)
        {
            break;
        }
    } 
    while (n < 1 );
    
    for (int i = 0; i < n; i++)
    {

        for (int j = 0; j < n; j++)
        {
            printf("#");
        }
        
    }

    printf("\n");

}