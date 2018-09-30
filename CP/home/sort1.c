
#include <stdlib.h>
#include <stdio.h>
int main(void)
{
        int i,temp,j,n,k;
	printf("\n enter number of items\n");
	scanf("%d",&n);
	int *A=malloc(n*sizeof( int));
	if(A==NULL)
	{
		printf("\n not enough space\n");
			exit(0);
	}
	printf("\n enter elemwnts\n");
	for(i=0;i<n;i++)
	{
		scanf("%d",&A[i]);
	}
for(i=0;i<n-1;i++)
{
        for(j=0;j<n-1;j++)
        {                                                                        
		if(A[j]>A[j+1])
                {
                        temp=A[j];
                A[j]=A[j+1];
                A[j+1]=temp;
  		}

 	}
	for(k=0;k<n;k++)
	{
		printf("\t%d",A[k]);
	}
	printf("\n iteration %d\n",i);
}

 for(i=0;i<n;i++)
{
printf("\t%d",A[i]);
}
}
