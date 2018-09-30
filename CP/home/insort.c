#include <stdio.h>
#include <stdlib.h>
int main(void)
{
	int i=0,j=0,temp,n,k;
	printf("\n enter size of array\n");
	scanf("%d",&n);
	int *a=malloc(n*sizeof(int));
	if(a==NULL)
	{
		printf("\n not enough memory\n");
	}

	printf("\n enter elements of array\n");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<n-1;i++)
	{
		if(a[i+1]<a[i])
		{
		
			for(j=i+1;j>=0;j--)
			{
				printf("iteration=%d\tj=%d\n",i,j);
				if(j==n-1)
				{
					j=n-2;
				}

				while(a[j+1]<a[j])
				{
					temp=a[j],
					a[j]=a[j+1];
					a[j+1]=temp;	

				}
				for(k=0;k<n;k++)                                                 {                                                                        printf("\t %d",a[k]);                                    }                                                                printf("\n");
			}
		}
	/*	for(k=0;k<n;k++)
		{
			printf("\t %d",a[k]);
		}
		printf("\n");
		*/

	}

	for(i=0;i<n;i++)
	{
		printf("\n%d",a[i]);
	}
	printf("\n");
}

