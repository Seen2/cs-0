#include <stdio.h>
#include <math.h>
int main(void)
{
        int n,i=0,m,s=0;
        printf("\nenter the number\n");
        scanf("%d",&n);
        m=n;
        while(n!=0)
        {
                n=n/10;

                i++;
        }
        int *a=malloc(i*sizeof(int));
        int l=i;
        i=0;
        n=m;

        while(n!=0)
        {

                a[i]=n%10;

                n=n/10;
                i++;
        }
        for(i=0;i<l;i++)
        {
                s=s+(pow(a[i],l));
        }
        if(m==s)
                printf("\n%d is armstrong number\n",m);
        else
                printf("\n %d is not armstrong number\n",m);
}
