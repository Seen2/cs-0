#include <stdio.h>
int main(int argc,char *argv[])
{
int i;
printf("\n number of arg passed=%d\n",argc);
for(i=0;i<argc;i++)
{

  printf("\n arg[%d]=%s\n",i,argv[i]);

}

return 0;
}
