#include <stdio.h>
bool t(int);
int main(void)
{
	int s=9;
	printf"%d",(t(s));
	s=0;
	printf("%d",t(s));
}
bool t(int x)
{
	if(x==9)
	{
		return false;
	}
	else
		return true;
}

