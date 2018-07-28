#include <stdio.h>
#include <string.h>
int main(void)
{
char fn[100];
FILE  *f;
printf("\n enter file name\n");
fgets(fn,100,stdin);
if(f==NULL)
{
printf("\n No such file\n");
exit(0);
}
f=fopen(fn,"r+");
fclose (f);
}
