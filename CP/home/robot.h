#include <stdio.h>


typedef struct robot
{
	char name[10];
	char color[10];

}robot;


void speak(struct robot r)
{
        printf("\nhi i am %s with %s in my mind\n",r.name,r.color);
	
	
}

void  print(struct robot r)
{
        printf("\nthis is %s with color of %s \n",r.name,r.color);
}


	
