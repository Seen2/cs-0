#include <stdio.h>
#include <stdlib.h>
int main(void)
{
	char s[10];
	FILE *fp;
	fp=fopen("xm.txt","w+");
	if(fp==NULL)
	{
		printf("\n error **\n");
		exit(0);
	}

	printf("\n enter your name\n");
	fgets(s,10,stdin);
	fflush(stdin);
	fputs(fp,s);
	printf("\n mame has been written");
	fclose(fp);
}
