#include <stdio.h>

int main(void)
{
	int s=0b00000001;
	printf("s=%i \n",s);
	s =s & 0b00000000;
	printf("after AND operation s=%i \n",s);
	s |= 0b00000001;
	printf("after OR operation s=%i \n",s);
	s =!(s);

	printf("after NOT operation s=%i \n",s);

	s= 1<< 0b00000011;

	printf("after SHIFT operation s=%i \n",s);
	s=0;
	s ^=( 1<< s);
	printf("after XOR operation s=%i \n",s);
	s ^=s; 
	printf("after itself XOR operation s=%i \n",s);
	s ^=!s; 
	printf("after itself XOR operation s=%i \n",s);
}
