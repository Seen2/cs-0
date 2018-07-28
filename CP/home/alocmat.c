#include <stdio.h>
#include <stdlib.h>
 
int main()
{
    int r , c , i, j;
    printf("\nenter order\n");
    scanf("%d %d",&r,&c);
 
    int **arr = (int **)malloc(r * sizeof(int *));
    for (i=0; i<r; i++)
         arr[i] = (int *)malloc(c * sizeof(int));
 
    // Note that arr[i][j] is same as *(*(arr+i)+j)
    printf("\n enter elements\n");
    for (i = 0; i <  r; i++)
      for (j = 0; j < c; j++)
         scanf("%d",&arr[i][j]);
 
    for (i = 0; i <  r; i++)
    { for (j = 0; j < c; j++)
      { printf("\t%d ", arr[i][j]);
      }
     printf("\n");
    }
    free(arr);
 
   /* Code for further processing and free the 
      dynamically allocated memory */
 
   return 0;
}
