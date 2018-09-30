#include <stdio.h>
int swap(int*,int*);
int main(void)
{
	int a=10,b=9;
	int *m,*n;
	m=&a;
	n=&b;
	printf("a=%d b=%d\n",a,b);
	swap(m,n);
	printf("\na= %d b=%d\n",a,b);
}
int swap(int *x,int *y)
{
	int temp;
	temp=*y;
	*y=*x;
	*x=temp;
	return 0;
}



