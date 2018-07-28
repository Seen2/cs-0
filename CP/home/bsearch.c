#include <stdio.h>
#include <stdlib.h>
int main(void)
{ 
	int A[100];
	int i,n,s,start,end,mid,flag=0;
	printf("\n enter the no. of elements in array\n");
	scanf("%d",&n);
	printf("\n enter the elements of array\n");
	for(i=0;i<n;i++)
	{
		scanf("%d",&A[i]);
	}
	printf("\n enter the item for search\n");
	scanf("%d",&s);
	start=0;
	end=n;
	mid=(start+end)/2;
	while(start!=end)
	{
		if(A[mid]==s)
		{
			printf("\n search completed\na[%d]=%d\n",mid,s);
			flag=1;
			exit(0);
		}
		else if(A[mid]>=s)
			end=mid;
		else
		{

			start=mid+1;
		}
		mid=(start+end)/2;
	}
	if(flag!=1)
		printf("\n search not found\n");
}


