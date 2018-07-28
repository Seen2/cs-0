

#include <stdio.h>
int main()
{
char ch;
printf("\n enter alphabet ");
scanf(" %c",&ch);
if(ch>90)
printf("\n inverse alphabet is %c",ch-32);
if(ch<=90)
printf("\n inverse alphabet is %c",ch+32);
return 0;
}
