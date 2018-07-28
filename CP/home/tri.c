#include <stdio.h>
#include <stdlib.h>
#include <math.h>


#define PI 3.14
int main(void)
{
int c,x;
float v,b;
v=(2*PI)/180;
printf("\nenter the choice\n1 for sin\n2for cos\n3fortan\n4for cot\n5for sec\n6 forcosec\n7 to exit\n");
scanf("%d",&c);
printf("\n enter value of angle in degrer\n");
scanf("%d",&x);
switch(c)
{
case 1:
b=sin(x*v);
printf("\nsin for %d is %f",x,b);
break;
case 2:
b=cos(v*x);                                                                                           printf("\ncos for %d is %f",x,b);
break;
case 3:
b=tan(v*x);
printf("\ntan for %d is %f",x,b);
break;
case 4:
b=1/tan(v*x);
printf("\ncot for %d is %f",x,b);
break;
case 5:
b=1/cos(v*x);
printf("\nsec for %d is %f",x,b);
break;
case 6:
b=1/sin(v*x);
printf("\ncosec for %d is %f",x,b);
break;
case 7:
exit(0);
default:
printf("\n enter valid choice");
}
}
