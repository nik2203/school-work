#include<stdio.h>
#include<stdlib.h>



typedef struct node{
	int data;
	struct node* prev;
	struct node* next;
}NODE;

typedef struct dlist{
	NODE* head;
	int no_node; //number of nodes in the linked list
}DLIST;


DLIST *init(){		//initialises a doubly linked list to conduct operations on
	DLIST *temp=(DLIST*)malloc(sizeof(DLIST));
	temp->head=NULL;
	temp->no_node=0;
	return temp;
}

NODE* create_node(int ele){	//used to create a node
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
	printf("The element was inserted successfully\n");
}

void insert_rear(DLIST *ptr,int ele){
	NODE *temp=create_node(ele);
	if(ptr->head==NULL){
		ptr->head=temp;
	}
	else{
		NODE *cur=ptr->head;
		while(cur->next!=NULL){
			cur=cur->next;
		}
		cur->next=temp;
		temp->prev=cur;
	}
	ptr->no_node++;
	printf("The element was inserted successfully\n");
}

void insert_between(DLIST *ptr,int ele,int pos){
	NODE *temp=create_node(ele);
	int count_pos=1;
	if(ptr->head==NULL){
		ptr->head=temp;
	}
	else if(ptr->no_node==1){
		insert_front(ptr,ele);
	}
	else if((pos>ptr->no_node && ptr->no_node>1)||pos<1){
		printf("Insertion position is out of range\n");
		return;
	}
	else{
		NODE *cur=ptr->head;
		NODE *prev=NULL;
		while(cur!=NULL && pos!=count_pos){
			prev=cur;
			cur=cur->next;
			count_pos++;
		}
		prev->next=temp;
		temp->prev=prev;
		temp->next=cur;
		cur->prev=temp;
	}
	printf("The element was inserted succesfully\n");
}

int delete_front(DLIST *ptr){
	if(ptr->head==NULL){
		return 9999;
	}
	NODE *first=ptr->head;
	if(first->next==NULL){
		int x=first->data;
		free(first);
		ptr->head=NULL;
		return x;
	}
	NODE *second=first->next;
	int x=first->data;
	second->prev=NULL;
	ptr->head=second;
	free(first);
	ptr->no_node--;
	return x;
}

int delete_rear(DLIST *ptr){
	int x;
	if(ptr->head==NULL){
		return 9999;
	}
	else if(ptr->no_node==1){
		x=ptr->head->data;
		free(ptr->head);
		ptr->head=NULL;
		ptr->no_node--;
		return x;
	}
	else{
		NODE *cur=ptr->head;
		NODE *prev=NULL;
		while(cur->next!=NULL){
			prev=cur;
			cur=cur->next;
		}
		prev->next=NULL;
		x=cur->data;
		free(cur);
		ptr->no_node--;
		return x;
	}
}

int delete_between(DLIST *ptr,int pos){
	int x,count=1;
	if(ptr->head==NULL){
		return 9999;
	}
	else if(ptr->no_node==1){
		x=delete_front(ptr);
	}
	else if(pos==ptr->no_node){
		x=delete_rear(ptr);
	}
	else{
		NODE *cur=ptr->head;
		NODE *prev=NULL;
		while(cur!=NULL &&pos!=count){
			prev=cur;
			cur=cur->next;
			count++;
		}
		prev->next=cur->next;
		cur->next->prev=prev;
		x=cur->data;
		free(cur);
		ptr->no_node--;
	}
	return x;
}

void display(DLIST *ptr){
	if(ptr->head==NULL){
		printf("List is empty\n");
	}
	else{
		NODE *cur=ptr->head;
		while(cur!=NULL){
			printf("%d\t",cur->data);
			cur=cur->next;
		}
		printf("\n");
	}
}


int main(){
    DLIST* list=NULL;
	list=init();
	int choice,ele,x,pos;
	while(1){
		printf("Enter your choice\n");
		printf("1.Insert at front\n2.Insert at rear\n3.Delete at front\n4.Delete at rear\n5.Insert at a position\n6.Delete at a particular position\n7.Display\n8.Search\n9.Count nodes\n10.Exit\n");
		scanf("%d",&choice);
		switch(choice){
			case 1: printf("Enter the element\n");
					scanf("%d",&ele);
					insert_front(list,ele);
					break;
			case 2: printf("Enter the element\n");
					scanf("%d",&ele);
					insert_rear(list,ele);
					break;
			case 3: x=delete_front(list);
					if(x==9999){
						printf("The list is empty\n");
					}
					else{
						printf("The deleted element is %d \n",x);
					}
					break;
			case 5: printf("Enter element and position\n");
					scanf("%d %d",&ele,&pos);
					insert_between(list,ele,pos);
					break;
			case 6: printf("Enter position to delete at\n");
					scanf("%d",&pos);
					x=delete_between(list,pos);
					if(x==9999){
						printf("\nThe list is empty\n");
					}
					else{
						printf("\nThe deleted element is %d \n");
					}
					break;
			case 7: printf("\nThe list is\n");
					display(list);
					break;
			
		}
	}
    return 0;
}
