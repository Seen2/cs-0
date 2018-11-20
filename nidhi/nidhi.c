#include <stdio.h>
#include <stdlib.h>
 
int main()
{
   char ch, file_name[25];
   FILE *fp;
 
   printf("Enter name of a file you wish to see\n");
   //In case for taking file name as input

   //fgets(file_name,25,stdin); //method:0 to take string as input but not work here
   scanf("%s",file_name); //best method:1 to take string as input but work here

   //scanf("%[^\n]%*c", file_name); method:2 to take string as input work here "GOOGLED" (:
 
   fp = fopen(file_name, "r"); // read mode

   //if no file found with name the below condition will execute
   if (fp == NULL)
   {
      perror("Error while opening the file.\n");
      exit(EXIT_FAILURE);
   }
 
   printf("The contents of %s file are:\n", file_name);
 
   //take each charector of file and print it continiously until 
   //EOF(for all file there is a charector that indicates file ends here) is found
   while((ch = fgetc(fp)) != EOF)
      printf("%c", ch); //print each charector
 
   fclose(fp); //close file to stay away from memory leakage while runing 
   return 0;
}









/*
#include <stdio.h>
#include <stdlib.h>
 
int main()
{
   char ch, file_name[25];
   FILE *fp;
 
   printf("Enter name of a file you wish to see\n");
   fgets(file_name,10,stdin);
   printf("The contents of %s file are:\n", file_name);
 
   fp = fopen(file_name, "r"); // read mode
 
   if (fp == NULL)
   {
      perror("Error while opening the file.\n");
      exit(EXIT_FAILURE);
   }
 
   printf("The contents of %s file are:\n", file_name);
   ch = fgetc(fp);
   while(ch  != EOF)
   {

      printf("%c", ch);
      ch = fgetc(fp);
   }

   fclose(fp);
   return 0;
}
*/
