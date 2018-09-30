#include <stdio.h>
#include <stdlib.h>
typedef struct node
{
	int n;
	struct node *next;
}node;
struct node *list;
struct node *newlist;
void dis(node*);
void insert(node*);
void search(node*);
void delete(node *);
struct node *first=NULL;
int main(void)
{
	int num,n,opt;
	struct node *ptr;
	int i=0;
	printf("\n enter number of item to create linked list\n");
	scanf("%d",&n);

	printf("\n enter the number\n");
	while(ptr!=NULL)
	{
		

	  scanf("%d",&num);
	  if(i==0)
	  {
	  first=malloc(sizeof(node));//alocating memory for node and addressing memory of node to the same pointer
	  list=first;//remembering pointer of first node
	  newlist=list;
	  first->n=num;//invoking data of node
	  first->next=malloc(sizeof(node));// allocating memory for next node to pointer of previous node
	  ptr=first->next;//invoking pointer of node
	  }

	  else
	  {
	   ptr->n=num;//passing or invoking data  value in node
	   if(i==n-1)
           {
                   ptr->next=NULL;// setting last pointer as null as end of list
		   ptr=ptr->next;//satisfying break condition for loop
           }
	   else
	   {
	   ptr->next=malloc(sizeof(node));// allocating memory for next node
	   ptr=ptr->next;//invoking pointer of next node
	   }
	   
	  }


	   i++;

          }
	printf("\n enter option\n 1 To insert\n 2 To search \n 3 to delete\n 4 to exit\n");
	scanf("%d",&opt);
	switch(opt)
	{
		case 1:
			insert(list);
			exit(0);
		case 2:
			search(list);
			break;
		case 3:
			delete(list);
			exit(0);
		case 4:
			printf("\n succesfully exited\n");
			exit(0);
		default:
			printf("ohh.. wrong option\n");
			exit(0);
	}


	  dis(newlist);

}


void dis(node *list)
{

	node *ptr=list;
	int i=0;
	
	
	while(ptr!=NULL)
	{
	
		printf("\n%d=%d",i,ptr->n);
		ptr=ptr->next;
		
		i++;
	}

}
void insert(node *list)
{
	int i=0,pos,data;
	int temp;
	node *newlist;
	newlist=list;
	node *ptemp;
		printf("\n enter position \n");
		scanf("%d",&pos);
		printf("\n enter data to insert\n");
		scanf("%d",&data);
		if(pos==i)
		{

			//ptemp=list;
			ptemp=malloc(sizeof(node));
			ptemp->n=data;
			ptemp->next=list;
			list=ptemp;
			dis(list);

			
		}
		else if(i<pos)
		{

		while(i!=pos)
		{
			
			if(i==pos-1)
			{
				if(list->next==NULL)
				{
					
					list->next=malloc(sizeof(node));
					list=list->next;
					list->n=data;
					list->next=NULL;
				}
				else
				{


				temp=list->n;

				ptemp=list->next;
				list->next=malloc(sizeof(node));//alocating memory for insertion

				list=list->next;//updating pointer of allocated memory
				list->n=data;//invoking  data in alocated memory
				list->next=ptemp;//invoking pointer in allocated memory
				list=list->next;//updating pointer variable for pre version

				
				printf("\n inserted\n");
				}
				dis(newlist);
			}
			else
			{
			list=list->next;//updating pointer
			}

			i++;
			
			
		}
		}
		else
		{
			printf("\n invalid try\n");
			dis(newlist);
		}

}
void search(node *list)
{
	int data,i=0;
	printf("\n enter data for search\n");
	scanf("%d",&data);
	if(list->n==data)
	{
		printf("\n search complete %dth=%d",i,data);
	}
	else
	{

	while(list->n!=data)
	{
		if(list->next==NULL)
		{
			printf("\n no element found");
			break;
		}
		else
		{

		list=list->next;
		if(list->n==data)
		{
			printf("\n search completed\n %d th data=%d",i+1,data);
		}
		}

		i++;

	}
	}
}
void delete(node *list)
{
	int pos,i=0;
	node *ptemp;
	node *newlist=list;

	printf("\n enter position you want to remove\n");
	scanf("%d",&pos);
	if(i==pos)
	{


			printf("\ni=pos\n");
		        ptemp=list;//taking new pointer and updating below
                        list=list->next;//here
                        free(ptemp);//deleting node with initial pointer
                       // list=ptemp;//giving value of new pointer to initial pointer
		       dis(list);

	}
	else
	{

	while(i!=pos)
	{
		
		i++;
		if(i==pos)
		{
			if(list==NULL)
			{
				free(list);
			}
			else
			{
			ptemp=list->next;//taking new pointer and updating below
			ptemp=ptemp->next;//here
			free(list->next);//deleting node with initial pointer
			list->next=ptemp;//giving value of new pointer to initial pointer
			}
			dis(newlist);
		}
		else if(list!=NULL)
		{
		list=list->next;
		}
		else
		{
			printf("\n element is not in list...\n");
			dis(newlist);
			break;
		}
		



	}
	}

}





		

	




