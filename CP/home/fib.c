#include <stdio.h>
long int fib(long int);
int main(void)
{
long int i,n,f;
printf("\n enter the number of terms\n");
scanf("%ld",&n);
f=fib(n);
for(i=0;i<n;i++)
{
printf("\n %ld is %ld",i,fib(i));
}
}
long int fib(long int x)
{
if(x==0)
return(0);
if(x==1)
return(1);
return(fib(x-1)+fib(x-2));

}
