#include <stdio.h>
void printTow(int,int);
void toh(int,int,int,int);
int main(void)
{
	int n;
	printf("\n enter the number of disc in Tower of hannoi\n");
	scanf("%d",&n);
	toh(n,1,2,3);

}

void toh(int n,int fr,int to,int sp)
{
	if(n==1)
	{
		printTow(fr,to);

	}
	else
	{
		toh(n-1,fr,sp,to);
		toh(1,fr,to,sp);
		toh(n-1,sp,to,fr);
	}

}

void printTow(int fr,int to)
{
	printf("\nmove from %d to %d \n ",fr,to);
}

