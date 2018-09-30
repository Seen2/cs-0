#include <stdio.h>
int main(void)
{
	int n,i;
	printf("\n enter number of students\n");
	scanf("%d",&n);
	typedef struct
	{
		int day;
		int month;
		int year;
	}DATE;

	struct student
	{
		char name[30];
		int roll;
		DATE dob;
	};
	struct student stud[50];
	for(i=0;i<n;i++)
	{
	printf("\nAbout stud %d\n enter student name and roll number\n",i+1);
	scanf("%s",stud[i].name);
	scanf("%d",&stud[i].roll);
	printf("\n enter date of birth\n");
	scanf("%d %d %d",&stud[i].dob.day,&stud[i].dob.month,&stud[i].dob.year);
	}
	for(i=0;i<n;i++)
	{
	printf("\nAbout student %d\n Name is %s \n Roll number is %d\n",i+1,stud[i].name,stud[i].roll);
	printf("\n Date of birth is %d/%d/%d\n",stud[i].dob.day,stud[i].dob.month,stud[i].dob.year);
	}
}
