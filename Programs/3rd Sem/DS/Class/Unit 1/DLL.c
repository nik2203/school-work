#include<stdio.h>
#include<stdlib.h>



typedef struct node{  //structure for node of a DLL
	int data;
	struct node* prev;
	struct node* next;
}NODE;

typedef struct dlist{ //structure for DLL
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
	temp=(NODE*)malloc(sizeof(NODE)); //dynamically allocates memory for a node
	temp->data=ele;
	temp->prev=temp->next=NULL;
	return(temp);
}

void insert_front(DLIST* ptr, int ele){ //function to insert a node at the front of a DLL
	NODE* temp = create_node(ele);  //temporary node that stores data value to be inserted
	if(ptr->head==NULL){
		ptr->head=temp;
	}
	else{
		NODE *first=ptr->head;
		first->prev=temp;
		temp->next=first;
		ptr->head=temp;
	}
	ptr->no_node++; //updates the no_node variable which stores the number of nodes in the linked list
	printf("The element was inserted successfully\n");
}

void insert_rear(DLIST *ptr,int ele){ //function to insert a node at the rear of a DLL
	NODE *temp=create_node(ele);
	if(ptr->head==NULL){
		ptr->head=temp;
	}
	else{
		NODE *cur=ptr->head;
		while(cur->next!=NULL){ //iterates through the list till last element is found
			cur=cur->next;
		}
		cur->next=temp;
		temp->prev=cur; //establishes link between temporary node and the list
	}
	ptr->no_node++;
	printf("The element was inserted successfully\n");
}

void insert_between(DLIST *ptr,int ele,int pos){  //function to insert a node at a particular position in a list
	//similar to the insert between function for SLL
	NODE *temp=create_node(ele);
	int count_pos=1; //counter to keep track of position in the list
	if(ptr->head==NULL){
		ptr->head=temp;
		temp->prev=ptr->head;
	}
	else if(ptr->no_node==1){
		insert_front(ptr,ele);
	}
	else if((pos>ptr->no_node && ptr->no_node>1)||pos<1){ //accounts for invalid position values
		printf("Insertion position is out of range\n");
		return;
	}
	else{
		NODE *cur=ptr->head;
		NODE *prev=NULL;
		while(cur!=NULL && pos!=count_pos){ //iterates through the list till either the end of list is reached or the desired postion for insertion
			prev=cur;
			cur=cur->next;
			count_pos++;
		}
		temp->next=cur;
		prev->next=temp;
		temp->prev=prev;
		cur->prev=temp;
	}
	printf("The element was inserted succesfully\n");
}

int delete_front(DLIST *ptr){  //function to delete a node from the rear of a list
	if(ptr->head==NULL){
		return 9999;
	}
	NODE *first=ptr->head; //pointer to the first node of the list
	if(first->next==NULL){  //case where there is only one node in the list
		int x=first->data;
		free(first);
		ptr->head=NULL;
		return x;
	}
	NODE *second=first->next; //pointer to the second node of the list
	int x=first->data;
	second->prev=NULL;
	ptr->head=second;
	free(first);
	ptr->no_node--;
	return x;
}

int delete_rear(DLIST *ptr){ //function to delete a node from the rear of the list
	int x;
	if(ptr->head==NULL){
		return 9999;
	}
	else if(ptr->no_node==1){  //case where only one element is in the list
		x=ptr->head->data;
		free(ptr->head);
		ptr->head=NULL;
		ptr->no_node--;
		return x;
	}
	else{
		NODE *cur=ptr->head;
		NODE *prev=NULL;
		while(cur->next!=NULL){ //iterates through the list till the last element is found
			prev=cur;
			cur=cur->next;
		}
		prev->next=NULL;
		x=cur->data;
		free(cur);
		ptr->no_node--; //decreases node count after node is deleted
		return x;
	}
}

int delete_between(DLIST *ptr,int pos){ //function to delete node between two nodes, i.e, at a particular position
	int x,count=1;
	if(ptr->head==NULL){
		return 9999;
	}
	//case for if the given position is the front or the end of the list
	else if(ptr->no_node==1){
		x=delete_front(ptr);
	}
	else if(pos==ptr->no_node){
		x=delete_rear(ptr);
	}
	else{
		NODE *cur=ptr->head;
		NODE *prev=NULL;
		while(cur!=NULL && pos!=count){ //iterates through list until end is reached or the specified position is reached
			prev=cur;
			cur=cur->next;
			count++;
		}
		prev->next=cur->next;
		cur->next->prev=prev;
		x=cur->data; //variable is given data value of the deleted node
		free(cur);
		ptr->no_node--;
	}
	return x;
}


//function to create an ordered list 
void order(DLIST *ptr,int ele,int choice){  //orders a list as it receives inputs
	NODE *temp=create_node(ele);
	if(ptr->head==NULL){  //if the list is empty, first element is added
		ptr->head=temp;
	}
	else{
		if(choice==1){  //option 1 is for ascending order
			NODE *first=ptr->head;
			NODE *prev=NULL;
			if(temp->data<first->data){ 
				temp->next=first;
				first->prev=temp;
				ptr->head=temp;
			}
			else{
				while(first->next!=NULL&&temp->data>first->next->data){ //iterates through list till a suitable position for insertion is found
					first=first->next;
				}
				temp->next=first->next;
				first->next=temp;
				temp->prev=first;
			}
		}
		else{ //option 2 is for descending order
			NODE *first=ptr->head;
			NODE *prev=NULL;
			if(temp->data>first->data){
				ptr->head=temp;
				temp->next=first;
				first->prev=temp;
			}
			while(first!=NULL&&temp->data<first->data){
				prev=first;
				first=first->next;
			}
			temp->next=first->next;
			first->next=temp;
			temp->prev=first;
		}
	}
}

//function to search in an ordered list

int search(DLIST *ptr,int ele){
	int count=1;
	NODE *cur=ptr->head;
	if(ptr->head==NULL){
		return 9999;
	}
	else{
		while(cur->next!=NULL){
			if(cur->data!=ele){
				cur=cur->next;
				count+=1;
			}
			else{
				return count;
			}
		}
	}
}


//function to merge two ordered lists
void merge_list(DLIST *ptr1, DLIST *ptr2){
	NODE *cur=ptr1->head;
	if(cur==NULL){
		NODE *cur1=ptr2->head;
		while(cur1!=NULL){
			order(ptr1,cur1->data,1);
			cur1=cur1->next;
		}
	}
	else{
		while(cur->next!=NULL){
			cur=cur->next;
		}
		cur->next=ptr2->head;
		ptr2->head->prev=cur;
	}
}

void display(DLIST *ptr){ //function to display the list
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

//menu driven part of the program to work with doubly linked lists

int main(){
    DLIST* list=NULL; //creates a list of DLIST type
	DLIST* list2=NULL;
	list=init(); //initialises the list
	int choice,ele,x,pos;
	while(1){
		printf("Enter your choice\n");
		printf("1.Insert at front\n2.Insert at rear\n3.Delete at front\n4.Delete at rear\n5.Insert at a position\n6.Delete at a particular position\n7.Display\n8.Insert into Ordered List\n9.Search in Ordered List\n10.Merge Two Ordered Lists\n11.Exit\n");
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
			case 8: int ord,no;
					printf("Select the ordering method:\n1.Ascending\n2.Descending\n");
					scanf("%d",&ord);
					if(ord==1||ord==2){
						printf("Enter the number of nodes in the list\n");
						scanf("%d",&no);
						for(int i=0;i<no;i++){
							printf("Enter the element to insert\n");
							scanf("%d",&ele);
							order(list,ele,ord);
						}
						printf("\n");
					}
					else{
						printf("Invalid option\n");
					}
					break;
			case 9: printf("Enter element to search for\n");
					scanf("%d",&ele);
					int ret=search(list,ele);
					if(ret==9999){
						printf("The list is empty\n");
					}
					else if(ret==0){
                        printf("The element was not found\n");
                    }
                    else{
						printf("The element %d was found at position %d\n",ele,ret);
					}
                    break;
			case 10:int ele_no,ele,c,i=0;
					list2=init();
					printf("How many elements do you want in the other list?\n");
					scanf("%d",&ele_no);
					if(ele_no==0){
						printf("The merged list is:\n");
						display(list);
						printf("\n");
					}
					else{
						printf("Enter the elements\n");
						for(i;i<ele_no;i++){
							printf("Enter the element\n");
							scanf("%d",&ele);
							order(list2,ele,1);
						}
						merge_list(list,list2);
						printf("The merged list is:\n");
						display(list);
						printf("\n");
					}
					break;
			case 11: exit(0);
			
		}
	}
    return 0;
}
