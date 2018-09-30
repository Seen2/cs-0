#include <stdio.h>
int gcd(int,int);
int main()
{
	int n,r,m;
	printf("\n enter the numbers\n");
	scanf("%d %d",&n,&m);
	r=gcd(n,m);
	printf("\n gcd is %d\n",r);
	return 0;
}
int gcd(int x,int y)
{
	if(x%y==0)
		return y;
	return(gcd(y,x%y));
}

