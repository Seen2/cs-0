#include <stdio.h>
#include <stdlib.h>
#include "sl.h"
int main()
{
int i,n=4;
struct student s[4];
for(i=0;i<n;i++)
{
printf("\n enter the name of student\n");
scanf("%s",s[i].name);

printf("\n enter roll number\n");
scanf("%d",&s[i].roll);
}

printf("\n here is list\n");
for(i=0;i<n;i++)
{
printf("\n student[%d]name %s\n student[%d]roll is %d",i,s[i].name,i,s[i].roll);

}
printf("\n");
return 0;
}
