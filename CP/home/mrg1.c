#include <stdio.h>
void devide(int a[],int,int);
void sort(int a[],int,int,int);
int main(void)
{
	int a[5]={5,4,3,2,1};
	int i;


	devide(a,0,4);
	



	for(i=0;i<5;i++)
	{
		printf("\n %d",a[i]);
	
	}


}
void  devide(int a[],int f,int size)
{
	int l;
	l=size;
	
	int k;

	if(f!=l)
	{

		m=(f+l)/2;
		devide(a,f,m);

		devide(a,m+1,size);
		sort(a,f,m,size);
	}
}
void sort(int a[],int f,int m,int size)
{
	int temp[size];
	int in=0;
	int i=0,j=f;
	while(i<m && j<size)
	{
		if(a[i]>a[j+1])
		{
			temp[in]=a[j+1];
			temp[in+1]=a[i];
			i++;
		}
		else
		{
			temp[in]=a[i];
			temp[in+1]=a[j+1];
			j++;
		}
		in++;
	}
}
			

