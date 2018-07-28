#include <stdio.h>
#include <stdlib.h>
int main(void)
{
	int *a=malloc(4*sizeof(int));
	int i;
	for(i=0;i<4;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<4;i++)
        {
                printf("%d\n",a[i]);
        }
	a=realloc(a,6);
	for(i=0;i<6;i++)
	{
		printf("%d\n",a[i]);
	}
	free(a);
}
