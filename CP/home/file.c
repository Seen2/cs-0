#include <stdio.h>
#include <string.h>
int main(void)
{
char n[10];
FILE* f;
printf("\n enter file name\n");
fgets(n,10,stdin);
f=fopen("%s",n,"w");
fprintf(f,"i m\n");
fclose(f);
}
