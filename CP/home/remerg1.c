#include <stdio.h>

int main()
{
	int i,temp,n,j;
	printf("\n enter number of elements\n");
	scanf("%d",&n);
	int *a=malloc(n*sizeof(int));

	int x=n;
	printf("\n enter the elements\n");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	

        while(x>1)
        {
          x=x/2;      

	for(i=0;i<x-1;i++)
	{
		for(j=0;j<x-1;j++)
		{
		if(a[i]>a[i+1])
		{
			temp=a[i];
			a[i]=a[i+1];
			a[i+1]=temp;
		}
		printf("\ta[%d]=%d",i,a[i]);
		}
	
	
	}
	int t;
	printf("\n");
	for(i=(x/2)+1;i<n-1;i++)
	{
		for(j=0;j<n-1;j++)
		{
			if(a[i]>a[i+1])
		{
			t=a[i];
			a[i]=a[i+1];
			a[i+1]=t;
		}
		printf("\ta[%d]=%d",i,a[i]);
		}
	}
	
	}
	printf("\n sorted array is\n");
	for(i=0;i<n;i++)
	{
		printf("\t%d",a[i]);
	}
	printf("\n");
	free(a);
	return 0;
}

