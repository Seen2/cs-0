#include <stdio.h>
int fact(int);
int main(void)
{
int n,f;
printf("\n enter number please\n");
scanf("%d",&n);
f=fact(n);
printf("\n factorial is %d",f);

}
int fact(int x)
{
if(x<=1)
return 1;
return(x*fact(x-1));
}
