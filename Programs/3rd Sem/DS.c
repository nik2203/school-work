#include<stdio.h>
#include<stdlib.h>

// Singly linked list code


/*typedef struct node{
	int data;
	struct node* link;
}NODE;

typedef struct llist{
	NODE * head;
}LLIST;

void init(LLIST *ptr){
	ptr->head=NULL;
}

NODE* create_node(int ele){
	NODE *temp;
	temp=(NODE*)malloc(sizeof(NODE));
	if(temp!=NULL){
		temp->data=ele;
	}
	return(temp);
}

void insert_front(LLIST *ptr, int ele){
	 NODE *temp;
	 temp=create_node(ele);
	 temp->link=ptr->head;
	 ptr->head=temp;
}

void insert_rear(LLIST *ptr,int ele){
	NODE *temp;
	temp=create_node(ele);
	NODE *cur=ptr->head;
	while(cur->link!=NULL){
		cur=cur->link;
	}
	temp->link=NULL;
	cur->link=temp;
}

void display(LLIST *ptr){
	NODE *cur=ptr->head;
	if(ptr->head==NULL){
		printf("List is empty\n");
	}
	else{
		while(cur!=NULL){
			printf("%d\t",cur->data);
			cur=cur->link;
		}
	}
	printf("\n");
}

int delete_front(LLIST *ptr){
	if(ptr->head == NULL){
		return 9999;
	}
	NODE *first = ptr->head;
	ptr->head = first->link;
	int x = first->data;
	free(first);
	return x;
}

int delete_rear(LLIST *ptr){
	NODE *cur=ptr->head;
	NODE *prev=NULL;
	if(ptr->head==NULL){
		return 9999;
	}
	while(cur!=NULL){
		prev=cur;
		cur=cur->link;
	}
	prev->link=NULL;
	int x=cur->data;
	free(cur);
	return x;
}

int search_list(LLIST *ptr,int ele){
	int count=1;
	NODE *cur=ptr->head;
	if(ptr->head==NULL){
		return 9999;
	}
	else{
		while(cur->link!=NULL){
			if(cur->data!=ele){
				cur=cur->link;
				count+=1;
			}
			else{
				return count;
			}
		}
	}
}

void count_node(LLIST *ptr){
	int count=1;
	NODE *cur=ptr->head;
	if(ptr->head==NULL){
		printf("Total number of nodes is 0\n");
	}
	else{
		while (cur->link!=NULL)
		{
			cur=cur->link;
			count+=1;
		}
		printf("Total number of nodes is %d\n",count);
		
	}
}
*/


//Main part of singly linked lists


/*	LLIST myList;
	init(&myList);
	int choice,ele;
	for(;;){
		printf("Enter your choice\n");
		printf("1.Insert at front\n2.Insert at rear\n3.Delete at front\n4.Delete at rear\n5.Display\n6.Search\n7.Count nodes\n8.Exit\n");
		scanf("%d",&choice);
		switch(choice){
			case 1: printf("Enter the element\n");
					scanf("%d",&ele);
					insert_front(&myList,ele);
					break;
			case 2: printf("Enter the element\n");
					scanf("%d",&ele);
					insert_rear(&myList,ele);
					break;
			case 3: int x = delete_front(&myList);
					if(x==9999){
						printf("The list is empty\n");
					}
					else{
						printf("Deleted element is %d\n",x);
					}
					break;
			case 4: x = delete_rear(&myList);
					if(x==9999){
						printf("The list is empty");
					}
					else{
						printf("Deleted element is %d\n",x);
					}
					break;
			case 5: display(&myList);
					break;
			case 6: printf("Enter element to search for\n");
					scanf("%d",&ele);
					int ret=search_list(&myList,ele);
					if(ret==9999){
						printf("The list is empty\n");
					}
					else{
						printf("The element %d was found at position %d\n",ele,ret);
					}
			case 7: count_node(&myList);
		}
	}

*/

typedef struct node{
	int data;
	struct node* prev;
	struct node* next;
}NODE;

typedef struct dlist{
	NODE* head;
	int no_node;
}DLIST;


DLIST *init(){
	DLIST *temp=(DLIST*)malloc(sizeof(DLIST));
	temp->head=NULL;
	temp->no_node=0;
	return temp;
}

NODE* create_node(int ele){
	NODE* temp;
	temp=(NODE*)malloc(sizeof(NODE));
	temp->data=ele;
	temp->prev=temp->next=NULL;
	return(temp);
}

void insert_front(DLIST* ptr, int ele){
	NODE* temp = create_node(ele);
	if(ptr->head==NULL){
		ptr->head=temp;
	}
	else{
		NODE *first=ptr->head;
		first->prev=temp;
		temp->next=first;
		ptr->head=temp;
	}
	ptr->no_node++;
}

void display(DLIST *ptr){
	if(ptr->head==NULL){
		printf("List is empty\n");
	}
	else{
		NODE *cur=ptr->head;
		while(cur!=NULL){
			printf("%d",cur->data);
			cur=cur->next;
		}
	}
}


int main(){
	DLIST* list=NULL;
	list=init();
	int choice,ele,x;
	while(1){
		printf("Enter your choice\n");
		printf("1.Insert at front\n2.Insert at rear\n3.Delete at front\n4.Delete at rear\n5.Insert at a position\n6.Delete at a particular position\n7.Display\n8.Search\n9.Count nodes\n10.Exit\n");
		scanf("%d",&choice);
		switch(choice){
			case 1: printf("Enter the element\n");
					scanf("%d",&ele);
					insert_front(list,ele);
					break;
			case 7: display(list);
					break;
			/*case 2: printf("Enter the element\n");
					scanf("%d\n",&ele);
					break;*/
		}
	}
	return 0;
}



	//int a[]={10,20,30};
	//int *ptr=a;
	//a++;
	//int q=*ptr++; //int q; q=ptr++; *ptr;
	//int r=*++ptr;
	//int s=++*ptr;
	
	//printf("%d %d\n",q,*ptr);