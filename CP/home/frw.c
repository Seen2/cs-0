#include <stdio.h>

#include <string.h>
int main()
{
int i=0,ch;
char a[100];
FILE *s;
s=fopen("x.c","a+");
if(s==NULL)
printf("\n file not found\n");

fprintf(s,"suraj bhaiya is bahubali");
while(1)
{
if(feof(s))
{
break;
}
ch=fgetc(s);
a[i]=(char)ch;
}
a[i]='\0';

puts(a);

fclose(s);

return 0;
}
