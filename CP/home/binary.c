#include <stdio.h>
#include <string.h>
int  main(void)
{
char str[100];
int i=0,A[1000],j,x[1000],y=0,B[1000],z,p;
long long int n;
printf("\n enter the string\n");
fgets(str,100,stdin);
for(p=0,z=strlen(str);p<z;p++)
{
x[i]=(int) str[i];

while(x[i]>=1)
{
B[y]=x[i]%2;
x[i]=x[i]/2;
y++; 
}
}
printf("\n enter the number");
scanf("%lld",&n);
if(n<0)
{
n=(-1)*(n);

while(n>=1)
{
A[i]=n%2;
n=n/2;
i++; 
}
A[i]=1;
}
while(n>=1)
{
A[i]=n%2;
n=n/2;
i++; 
}
printf("\n your binary for number and string are \n");
int k=i;
for(j=0;j<=i;j++)
{
printf("%d",A[k]);
k=k-1;
}
printf("\n");
 k=y;
for(j=0;j<=y;j++)
{
printf("%d",B[k]);
k=k-1;
}
}
