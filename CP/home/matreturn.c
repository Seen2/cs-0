#include <stdio.h>
int rturn(int);
int main()
{
	int m,n,i,j;
	printf("\n enter order of matrix\n");
	scanf("%d %d",&m,&n);
	int **mat=malloc(m*sizeof(int*));
	for(i=0;i<m;i++)
	{
		mat[i]=malloc(n*sizeof(int));
	}


	printf("\n enter matrix\n");
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			scanf("%d",&mat[i][j]);
			a=rturn(mat[i][j]);
		}
	}
	
	
	printf("\n here is yours\n");
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			printf("\t%d",mat[i][j]);
		}
		printf("\n");
	}
	free(mat);
	printf("\n");
	return 0;
}
