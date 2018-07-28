#include <stdio.h>
#include <string.h>
int main(void)
{
char s1[20],s2[20];
printf("\n enter string\n");
fgets(s1,20,stdin);
strcpy(s2,s1);
puts(s2);
}
