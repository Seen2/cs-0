#include <stdio.h>
int main(void)
{
	int *a=malloc(sizeof(int));
	printf("adress=%u , %d",a,*a);
	*a=10;
	printf("*a=%d,add=%u",*a,a);
	free(a);
	printf("*a=%d,add=%u",*a,a);
}
