#include <stdio.h>
#include <string.h>
int main(void)
{
	struct class
	{
		char name[20];
		int roll;
	};
        struct	class s1;
	printf("\n enter name\n");
	fgets(s1.name,20,stdin);
	printf("\n enter roll number\n");
	scanf("%d",&s1.roll);
	printf("\n Name is\n");
	puts(s1.name);
	printf("\n roll number is %d",s1.roll);
}
