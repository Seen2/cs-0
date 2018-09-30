#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
float fn(float);
int main(void)
{
    float a,b,c;
    float i1,i2;
    printf("\n solution for x^2-x-3.75");
    printf("\n enter the interval \n");
    scanf("%f %f",&a,&b);
    c=a;
    i1=fn(a);
    i2=fn(b);
    if(i1*i2>0)
    {
        printf("\n f(a)*f(b)=%f interval is not sutaible",i1*i2);
        exit(0);
    }    
    else if(i1*i2==0)
        {
            printf("\n solution exit");
            if(i1==0 && i2==0)
            {
                printf("\n %f and %f is solution",a,b);
                exit(0);
            }
                if(i1==0)
            {
                printf("\n %f is solution");
            }
            else
            printf("\n %f is solution",b);
        exit(0);            
        }
    while(fn(a)!=0)
    {
        i1=fn(a);
        i2=fn(b);    
         if(i1*i2>0)
        {
            b=a;
            a=c;    
        }
        else
        a=(a+b)/2;
    }
    printf("\n solution exit");
    printf("\n solution is %f",a);
    getch();
}
float fn(float x)
{
    float d;
    d=x*x-x-3.75;
    return d;
}