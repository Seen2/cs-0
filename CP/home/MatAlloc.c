#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int m,n,i,j;
	int *a=malloc(sizeof(int));
	printf("\n enter row:");
	scanf("%d",&m);
	printf("\n enter column:");
	scanf("%d",&n);


	//int *ma=malloc(n*sizeof(int));
	int *(*ma)=NULL;
	for(i=0;i<n;i++)
	{
		int *(*ma)=malloc(m*sizeof(int));

	}

	printf("\n enter matrix\n");

	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			scanf("%d",&ma[i][j]);
		}
	}
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			printf("\t %d",ma[i][j]);
		}
		printf("\n");
	}

	printf("\n");

	free(ma);

}

