#include <stdio.h>
int find_even(int k);

int main(void)
{
	int k;
	scanf("%i",&k);
	find_even(k);
}


int find_even(int k)
{
	int input=0,i=0,flag=0,s[100];
	while(input!=-1)
	{
		scanf("%i",&input);
		s[i]=input;
		i++;
	}
	i=0;
	while(s[i]!=-1)
	{
		if(s[i]%2==0)
		{
			flag++;
		}
		if(flag==k)
		{
			printf("%i",s[i]);
			break;
		}
		i++;

	}
	if(i<k)
	{
		printf("%d",s[i]);
	}

}
