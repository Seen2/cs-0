#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main (void)
{
int n;
printf("\n enter the length of string\n");
scanf("%d",&n);
char* w=malloc(n*sizeof(char));
printf("\n enter the string\n");
scanf("%s",w);
printf("\n legth of string is %d\n string is\n",strlen(w));
puts(w);

}

