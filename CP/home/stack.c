#include <stdio.h>
#include <stdlib.h>

int pop(int);
int push(int);
int display(int);
int M=8;
int stack[8];
int top=0;
int main(void)
{
    int item,opt,i;
    printf("\n enter the option below\n");
    printf("\n 1 for push\n 2 for pop \n 3 to display\n 4 to exit\n");
    scanf("%d",&opt);
    switch(opt)
    {
              case 1: 
               while(i<M)
              {
                 printf("\n enter the value to push\n");
                         scanf("%d",&item);
                          i=push(item);
              }
              if(i>=M)
              return main();
              case 2:
                   while(i>=0)
                   {
                    printf("\n enter the value to pop\n");
                         scanf("%d",&item);
                          i=pop(item);
                    }
                    if(i==-1)
                         return main();
              case 3:
                   i=display(top);
                   if(i==-1)
		   {
			   printf("\n nothing to dispay\n");
		   }
                   
              break;
              case 4:
                   exit(0);
                   
              default:
                      return main();
    }
}

int push(int x)
{
    stack[top]=x;
    top=top+1;
             return top;
    
}
int pop(int x)
{
    x=stack[top];
    top=top-1;
    if(top>=0)
    {
             return top;
    }
    else
    printf("\n stack under flow\n");
    return top;
}
int display(int x)
{
    int i;
    for(i=0;i<=x;i++)
    {
                    printf("\n stack[%d]=%d",i,stack[i]);
    }
    if(x==-1)
	    return -1;
    return 0;
}
