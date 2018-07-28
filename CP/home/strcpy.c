#include <stdio.h>
#include <string.h>
int main(void)
{
char s[20],s1[25];
int i,l;
printf("\n enter the string\n");
fgets(s,20,stdin);
printf("\n here is entered string\n");
puts(s);
l=strlen(s);
printf("\n here is capitalization view\n");
for(i=0;i<l;i++)
{
if((int)s[i]>=97)
{
s1[i]=(char)((int)s[i]-32);
}
else
s1[i]=s[i];
}
puts(s1);
}
