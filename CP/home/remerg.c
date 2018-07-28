#include <stdio.h>

int sort(int b[],int size);
int main(void)
{
	int a[5]={4,9,3,5,8};
	int s,i,temp,b[5];
	s=sort(b[],5);
	for(i=0;i<5;i++)
	{    if(sort(b[i])>sort(b[i+1]))

		{
			temp=a[i];
			a[i]=a[i+1];
			a[i+1]=temp;
		}
	}
	for(i=0;i<5;i++)
	{
		printf("\t%d",a[i]);
	}
}
int sort(int b[],int size)
{
	if(size==1)
		return (b[],1);


	return (sort(b[],size/2));
}
