#include <stdio.h>
#include <stdlib.h>
int main(void)
{
	int i,j,small=1111111,n,temp,k,l;
	printf("\n enter the number of items in array\n");
	scanf("%d",&n);
	int *a=malloc(n*sizeof(int));

	if(a==NULL)
	{
		printf("\n no space");
		exit(0);
	} 

	printf("\n enter elements of array\n");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}

	for(i=0;i<n;i++)
	{
		
		for(k=i;k<n;k++)
        {
                if(a[k]<small)
                {
                        small=a[k];
			j=k;
                }
        }
		
		
		temp=a[i];
		a[i]=small;
		a[j]=temp;
		small=1111111;
		for(l=0;l<n;l++)
		{
			printf("\t %d",a[l]);
		}
		printf("\n iteration=%d\n",i);



	}


	for(i=0;i<n;i++)
	{
		printf("\t%d",a[i]);
	}
	printf("\n");
}

