#include <stdio.h>
int main(int a,char *arr[])
{
	int i;
	printf("\n %d\n",a);
	for(i=0;i<a;i++)
	{
		printf("\n %s\n",arr[i]);
	}
}
