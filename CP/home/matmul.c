#include <stdio.h>
#include <stdlib.h>

int main(void)
{
int m1[10][10],m2[10][10],m3[10][10],m,n,p,q,i,j,k,s;
printf("\n enter the order of matrix\n");
scanf("%d %d",&m,&n);
printf("\n enter matrix\n");
for(i=0;i<m;i++)
{
for(j=0;j<n;j++)
{
scanf("%d",&m1[i][j]);
}
}
printf("\n enter order of second matrix\n");
scanf("%d %d",&p,&q);
if(p!=n)
{
printf("\n invalid multiplication");
exit(0);
}
printf("\n enter second matrix element\n");
for(i=0;i<p;i++)
{
for(j=0;j<q;j++)
{
scanf("%d",&m2[i][j]);
}
}
for(i=0;i<m;i++)
{
for(j=0;j<p;j++)
{
s=0;
for(k=0;k<n;k++)
{
s=s+(m1[i][k])*(m2[k][j]);
}
m3[i][j]=s;
}
}

for(i=0;i<m;i++)
{
for(j=0;j<q;j++)
{
printf("\t%d",m3[i][j]);
}
printf("\n");
}

}
