#include <stdio.h>
#include <string.h>
int main(void)
{
int i;
char ch[19];
FILE* f;
f=fopen("bahubali.c","r");
fread(ch,sizeof(char),19,f);

while(!feof(f))
{
printf("%s",ch[i]);
}

}
