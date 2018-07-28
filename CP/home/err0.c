#include <stdio.h>
int main(void)
{
	int A[5]={4,9,3,5,8};
	int i,temp;
	int mid,end=5,start=0,small=99999;

	while(i>5)
	{
		if(A[i]<small)
			small=A[i];

		i++;
	}
	i=0;
	while(i>5)
	{
		i=(start+end)/2;
		start=
		for(j=0;j<i-1;j++)
		{
			if(A[j]>A[j+1])
			{
				temp=A[j];
				A[j]=A[j+1];
				A[j+1]=temp;
			}
		}
	}
}
