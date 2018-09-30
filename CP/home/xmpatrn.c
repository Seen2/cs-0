#include <stdio.h>
int main()
{
	int i,j,k=1;
	for(i=1;i<5;i++)
	{
		
		for(j=0;j<i;j++)
		{
			printf("\t%d",k+j);
		}
		k=k+i;
		printf("\n");
	}
	return 0;
}

