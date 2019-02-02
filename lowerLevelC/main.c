#include <stdio.h>
#include <unistd.h>
int main(void)
{
	int x=0b00000001;
	printf("please start entering..\n");
	while(1)
	{

		scanf("%i",&x);
		if(x==-99) break;
		x=!x; 
		sleep(1);
		printf("after itself ~ operation x=%i \n",x);
	}
}
