#include <stdio.h>
#include <string.h>
int main(int argc,char *argv[])
{
	int i;
	printf("\n %d",argc);
	for(i=0;i<argc;i++)
	{
		printf("\n%s",argv[i]);
	}

	return 0;
}
