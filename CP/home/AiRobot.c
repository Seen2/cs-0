#include <stdio.h>
#include "robot.h"

int main(void)
{
	struct robot r;
	printf("\nenter name:");

	scanf("%s",r.name);
	printf("\n enter color:");

	scanf("%s",r.color);
	printf("\n");
	print(r);
	speak(r);
	printf("\nDone with c\n");
}
