#include <stdio.h>
#include <stdlib.h>
int main(void)
{
	int a[100];
	int start=0,end,middle,n,key,i;
	printf("\n enter the number of elements\n");
	scanf("%d",&n);
	printf("\n enter elements in sorted form\n");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	printf("\n enter element to search\n");
	scanf("%d",&key);
	end=n-1;
	middle=(start+end)/2;
	while(key!=a[middle] && start<end && end>=0 )
	{
		if(key>a[middle])
		{
			start=middle+1;
		}
		else if(key<a[middle])
			
			end=middle-1;
		        


		else

		{
                      printf("element not found\n");
		      exit(0);
		}


		middle=(start+end)/2;
	}
	if(key==a[middle])
	{
		printf("\n search complete a[%d]=%d\n",middle,key);
	}
	else
		printf("element not found\n");
}

