#include <stdio.h>
#include <string.h>
int main(void)
{
char s[20];
printf("\nenter string\n");
fgets(s,20,stdin);
int l=strlen(s),i;
printf("\n %d\n",l);
for(i=0;i<l-1;i++)
{
printf("%d",(int)s[i]);
}
}
