#include<stdio.h>
#include<stdlib.h>



typedef struct node{   //defines the structure of a node
	int data;
	struct node* link;
}NODE;

typedef struct stack{  //defines the list and creates head node
	NODE * head;
}STACK;

void init(STACK *ptr){ //initialises a linked list
	ptr->head=NULL;
}

NODE* create_node(int ele){  //function to create node where data is a user defined value
	NODE *temp;
	temp=(NODE*)malloc(sizeof(NODE));  //dynamically assigns memory for the node
	if(temp!=NULL){
		temp->data=ele;
	}
	return(temp);
}

void push(STACK *ptr,int ele){  //func to insert a node at the rear of the linked list
	NODE *temp;
	temp=create_node(ele);
	NODE *cur=ptr->head;  //cur is the current node
	if(ptr->head==NULL){
		ptr->head=temp;
		temp->link=NULL;
	}
	else{
		while(cur->link!=NULL){
			cur=cur->link;
		}
		temp->link=NULL;
		cur->link=temp;
	}
}

void display(STACK *ptr){  //func to display all the nodes of the linked list
	NODE *cur=ptr->head;  
	if(ptr->head==NULL){
		printf("List is empty\n");
	}
	else{
		while(cur!=NULL){
			cur=cur->link;
		}
        printf("%d\t",cur->data);
	}
	printf("\n");
}

int delete_front(STACK *ptr){  //func to delete node at the front of the linked list
	if(ptr->head == NULL){
		return 9999; //9999 return code to indicate failure
	}
	NODE *first = ptr->head;
	ptr->head = first->link;
	int x = first->data;  //variable to store data of deleted node
	first->link=NULL;
	free(first); //deletes node
	return x;
}

int pop(STACK *ptr){ //func to delete node at the rear of the linked list
	NODE *cur=ptr->head;
	NODE *prev=NULL;
	if(ptr->head==NULL){
		return 9999;
	}
	else if(cur->link==NULL){
		int x = delete_front(ptr);
		return x;
	}
	else{
		while(cur->link!=NULL){
			prev=cur;
			cur=cur->link;
		}
		prev->link=NULL;  //assigns previous node's link to NULL, severing the connection between previous node and current node
		int x=cur->data;
		free(cur);
		return x;
	}
}

int main(){
	STACK mystack; //creates a list myList of LList type
	init(&mystack); //initialises myList
	int choice,ele,x;
	for(;;){
		printf("Enter your choice\n");
		printf("1.Push into stack\n2.Pop from stack\n3.Peek\n4.Exit\n");
        //Accepts choice from user for what operation to conduct
        scanf("%d",&choice);
		switch(choice){
			case 1: printf("Enter the element\n");
					scanf("%d",&ele);
					insert_rear(&mystack,ele);
                    printf("Element was successfully inserted\n");
					break;
			case 2: x = delete_rear(&mystack);
					if(x==9999){
						printf("The list is empty\n");
					}
					else{
						printf("Deleted element is %d\n",x);
					}
					break;
			case 3: printf("The list is:\n");
                    display(&mystack);
					break;
            case 4: exit(0);
		}
	}
    return 0;
}