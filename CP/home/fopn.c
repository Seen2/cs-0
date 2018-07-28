#include <stdio.h>
#include <stdlib.h>
int main()
{
	FILE *fp;
	char s[15],ch;
	printf("\n enter file name\n");
	fgets(s,15,stdin);
	fp=fopen(s,"r");
	if(fp==NULL)
	{
		printf("errror\n");
		exit(0);
	}
	
	while((ch=fgetc(fp))!=EOF)
	{
		ch=fgetc(fp);
		printf("%c",ch);
	}

	fclose(fp);

	return 0;
}
