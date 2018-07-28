//Bisection
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
float fn(float);
int main(void)
{
    float a,b,c,temp;
    float i1,i2;
    float k;
    printf("\n solution for x^2-x-3.75");
    printf("\n enter the interval \n");
    scanf("%f %f",&a,&b);
    if(a<0)
    {
	    temp=a;
	    a=b;
	    b=temp;
    }
    
    c=a;
    i1=fn(a);
    i2=fn(b);
    if(i1*i2>0)
    {
        printf("\n interval is not sutaible");
        exit(0);
    }    
    else if(i1*i2==0)
        {
            printf("\n solution exist");
            if(i1==0 && i2==0)
            {
                printf("\n %f and %f is solution",a,b);
                exit(0);
            }
                if(i1==0)
            {
                printf("\n %f is solution",a);
            }
            else
            printf("\n %f is solution",b);
        exit(0);            
        }
    int i=0;
    while(fabs(fn(a))>0.0001 && k!=a)
    {
	    i++;
	    printf("\niteration=%d\n",i);
        i1=fn(a);
        i2=fn(b);
	if(i1-i2==0)
	{
		printf("\n exceptio of 1/0=...\n");
		exit(0);
	}
         if(i1*i2>0)
        {
            b=a;
            a=c;    
        }
        else
	{
		k=a;
		
          a=(a*i2-b*i1)/(i2-i1);
	  
	}

    }
    printf("\n solution exist");
    printf("\n solution are %f",a);
}
float fn(float x)
{
    float d;
    d=x*x-x-3.75;
    return d;
}
