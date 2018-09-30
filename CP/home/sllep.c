// over flow



#include <stdio.h>
#include <unistd.h>
#include <math.h>

int main(void)
{
	int i;
	for(i=1;;i*2)
	{
		printf("\n%d\n is",i);
		printf("\n%d",i*2);
		sleep(1);
	}
}
