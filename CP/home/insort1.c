#include <stdio.h>
int main()
{
	int a[5]={2,1,7,5,4};
	int i,j,temp;

	for(j=0;j<5;j++)
	{

		while(a[j]>a[j+1])
		{

	for(i=0;i<5;i++)
	{
		if(a[i]>a[i+1])
		{
			temp=a[i];
			a[i]=a[i+1];
			a[i+1]=temp;
		}
	}
		}
	}

	for(i=0;i<5;i++)
	{
		printf("\t%d",a[i]);
	}
	return 0;

}
