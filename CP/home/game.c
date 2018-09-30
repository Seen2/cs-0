#include <stdio.h>
#include <math.h>
int main(void)
{
	int c=5,n=5,t;
	char name[20];
	int x,y,xc,yc;
	printf("\n enter your name\n");
	fgets(name,20,stdin);
	printf("hey %s\nRules of game\n1.you have to enter cordinates for landing your ship\n2.computer had already landed\n if your ship crash computer's ship you get one point and computer loose onepoint\nLETS BEGIN\n",name);

	while(c!=0 && n!=0)
	{
	printf("\nSCORE CARD\n%s=%d\tcomputer=%d\n",name,n,c);
	printf("\n enter cordinate for 2d\n");
	scanf("%d %d",&x,&y);

	xc=rand() %2;
	yc=rand() %2;
	printf("\n%s =(%d,%d)",name,x,y);

	printf("\tcomputer=(%d,%d)\n",xc,yc);
	if(xc==x && yc==y)
	{
		c--;
	}
	}
	if(c==0 || n==5)
	{
		printf("\n%s win\n score=%d\nGAME OVER\n",name,n);
	}
	if(n==0)
	{
		printf("\n you loose\n to try again press 1\n");
		scanf("%d",&t);
		if(t==1)
		{
			return main();
		}
	}
}
	

	
