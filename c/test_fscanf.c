#include <stdio.h>  
#include <stdlib.h>  

int main(void)  
{  
    int i;  
    printf("Input an integer:");  
    /*read an integer from the standard input stream*/  
    if (fscanf(stdin,"%d",&i))  
    {  
        printf("The integer read was :%d\n",i);  
    }   
    else  
    {  
        fprintf(stderr,"Error reading an integer from stdin.\n");  
        exit(1);  
    }  
    return 0;  
}  
