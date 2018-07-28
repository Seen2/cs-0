#include <stdio.h>
double sort(int B[],int size);
int main (void)
{
	int A[5]={4,9,3,5,8};
	double s;
	s=sort(A,5);
}
double sort(int B[],int size)
{
	int i;
	for(i=0;i<size;i++)
	{
		printf("\n %d",B[i]);
	}
	return 0;
}

