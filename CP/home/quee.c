#include <stdio.h>
#include <stdlib.h>
int max=5;
int enq(int,int);
int displ();
int R=0;
int F=0;
int quee[5];
int deq(int,int);
int main(void)
{
	int opt,item,c,i;
	printf("\n enter 1 For enq\nenter 2 for deq\nenter 3 to exit\n");
	scanf("%d",&opt);
	switch(opt)
	{
		case 1:
			printf("\n enter items to add\n");
			for(i=0;i<max;i++)
			{
				scanf("%d",&item);
			       c= enq(item,i);
			       if(c>=max)
			       {
				       printf("\n quee is full..\n here it is\n");
				       displ();
			       }
			}
			

		case 2:
			printf("\n enter item to dwquee\n");
			scanf("%d",&item);
			for(i=0;i<max;i++)
			{
				c=deq(item,i);
				if(F>R || F==0)
				{
					printf("\n quee is empty..");
					exit(0);
				}
			}
		case 3:
			exit(0);
		default :
			printf("\n invalid choice\n");
			return main();
	}


}
int enq(int x,int y)
{

	
	quee[y]=x;
	R=R+1;
	return R;
}
int deq(int x,int y)
{
	x=quee[y];
	F=F+1;
	return F;
}
int displ()

{
	int i;
	for(i=0;i<max;i++)
	{
		printf("\n%d",quee[i]);
	}
	return main();
}

 
