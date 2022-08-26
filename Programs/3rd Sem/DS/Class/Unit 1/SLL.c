#include<stdio.h>
#include<stdlib.h>



typedef struct node{   //defines the structure of a node
	int data;
	struct node* link;
}NODE;

typedef struct llist{  //defines the list and creates head node
	NODE * head;
}LLIST;

void init(LLIST *ptr){ //initialises a linked list
	ptr->head=NULL;
}

NODE* create_node(int ele){  //function to create node where data is a user defined value
	NODE *temp;
	temp=(NODE*)malloc(sizeof(NODE));
	if(temp!=NULL){
		temp->data=ele;
	}
	return(temp);
}

void insert_front(LLIST *ptr, int ele){  //function to insert a node at the front of the linked list
	NODE *temp;
	temp=create_node(ele);
	temp->link=ptr->head;
	ptr->head=temp;
}

void insert_rear(LLIST *ptr,int ele){  //func to insert a node at the rear of the linked list
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

void display(LLIST *ptr){  //func to display all the nodes of the linked list
	NODE *cur=ptr->head;  
	if(ptr->head==NULL){
		printf("List is empty\n");
	}
	else{
		while(cur!=NULL){
			printf("%d\t",cur->data); //prints data element of current node
			cur=cur->link;
		}
	}
	printf("\n");
}

int count_node(LLIST *ptr){   //func to count total number of nodes in the linked list
	int count=1;
	NODE *cur=ptr->head;
	if(ptr->head==NULL){
		return 9999;
	}
	else{
		while (cur->link!=NULL)
		{
			cur=cur->link;
			count+=1;  //update count after iterating through node
		}
		return count;		
	}
}

int delete_front(LLIST *ptr){  //func to delete node at the front of the linked list
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

int delete_rear(LLIST *ptr){//func to delete node at the rear of the linked list
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
		prev->link=NULL;
		int x=cur->data;
		free(cur);
		return x;
	}
}


//function to delete alternate nodes of a linked list starting from the first node
void delete_alternate(LLIST *ptr){
	int count=1;
	int total=count_node(ptr);
	NODE *cur=ptr->head;
	if(ptr->head==NULL){
		printf("The list is empty\n");
		return;
	}
	else if(total==1){
		delete_front(ptr);
		return;
	}
	else{
		NODE *prev=NULL;
		while(cur->link!=NULL){
			if(count%2==0){
				prev=cur;
				cur=cur->link;
				count++;
			}
			else if(count==1){
				prev=cur;
				cur=cur->link;
				ptr->head=cur;
				prev->link=NULL;
				free(prev);
				count++;
			}
			else{
				NODE *temp=cur;
				cur=cur->link;
				prev->link=cur;
				temp->link=NULL;
				free(temp);
				count++;
			}
		}
		if(total%2==1){
			prev->link=NULL;
			free(cur);
		}
	}
}

int search_list(LLIST *ptr,int ele){  //func to search list for node with specific element
	int count=1;  //variable to keep track of what node is currently being pointed to
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

//Assignment question: WAF to insert a node in between a particular node
//pos=position
void insert_between(LLIST *ptr,int pos,int ele){
    NODE *temp=create_node(ele);
    int count=1;
    if(ptr->head==NULL){
        ptr->head=temp;
        temp->link=NULL;
    }
    else if(count_node(ptr)==1){
        insert_front(ptr,ele);
    }
    else if((pos>count_node(ptr) && count_node(ptr)>1)||pos<1){
        printf("Given position is out of range\n");
        return;
    }
    else{
        NODE *cur=ptr->head;
        NODE *prev=NULL;
        while(cur!=NULL && count!=pos){
            prev=cur;
            cur=cur->link;
            count++;
        }
        prev->link=temp;
        temp->link=cur;
    }
}

/*int reverse_list(LLIST *ptr1, LLIST *ptr2){  // alternate, less efficient, func to reverse list
    //*ptr2 is pointer to second list which is going to accept values from initial linked list in reverse
    NODE *cur=ptr1->head;
    if(ptr1->head==NULL){
        return 9999;
    }
    else{
        while(cur!=NULL){
            insert_front(ptr2,cur->data);
             //by iterating through list 1 and inserting at the front of list 2, the reverse of list 1 is obtained in list 2
            cur=cur->link;
        }
        return 0;
    }
}*/

//Assignment question: WAP to reverse a linked list

int reverse_list(LLIST *ptr){ //func to reverse list
    NODE *cur=ptr->head;
    NODE *prev=NULL;  //initialises pointer to store previous node
    NODE *next=NULL;  //initialises pointer to store next node
    if(ptr->head==NULL){
        return 9999;
    }
    else{
        while(cur!=NULL){
            next=cur->link; //stores next node in next
            cur->link=prev; //makes link part of current node point to previous node;
            prev=cur; //moves pointer to previous node up to current node
            cur=next;  //moves pointer to current node up to next node
        }
        //loop ends when current node is NULL, signalling that end of linked list has been reached
        //now prev is the last element of the list and all links have been reversed
        ptr->head=prev; //assigns head to point to the last element of the list
        return 0;
    }
}

void merge_list(LLIST *ptr1,LLIST *ptr2){
	NODE *cur=ptr1->head;
	if(cur==NULL){
		NODE *cur1=ptr2->head;
		while(cur1!=NULL){
			insert_rear(ptr1,cur1->data);
			cur1=cur1->link;
		}
	}
	else{
		while(cur->link!=NULL){
			cur=cur->link;
		}
		cur->link=ptr2->head;
	}
}

/*void order_list(LLIST *ptr,int ord){
	int size=count_node(ptr);
	printf("%d\n\n",size);
	int i,j,ele;
	if(ord==1){
		for(i=0; i<size-1; i++){
			NODE *cur=ptr->head;
			for(j=0; j<size-i-1; j++){
				if(cur->data > cur->link->data){
					ele=cur->data;
					cur->data=cur->link->data;
					cur->link->data=ele;
				}
				cur=cur->link;
			}
		}
	}
	else if(ord==2){
		for(i=0; i<size-1; i++){
			NODE *cur=ptr->head;
			for(j=0; j<size-i-1; j++){
				if(cur->data < cur->link->data){
					ele=cur->data;
					cur->data=cur->link->data;
					cur->link->data=ele;
				}
				cur=cur->link;
			}
		}
	}
	else{
		printf("Invalid input\n");
		return;
	}	
}*/

void order(LLIST *ptr,int ele,int choice){
	NODE *temp=create_node(ele);
	if(ptr->head==NULL){
		ptr->head=temp;
		temp->link=NULL;
	}
	else{
		if(choice==1){
			NODE *first=ptr->head;
			NODE *prev=NULL;
			if(temp->data<first->data){
				temp->link=first;
				ptr->head=temp;
			}
			while(first!=NULL&&temp->data>first->data){
				prev=first;
				first=first->link;
			}
			prev->link=temp;
			temp->link=first;
		}
		else if(choice==2){
			NODE *first=ptr->head;
			NODE *prev=NULL;
			if(temp->data>first->data){
				temp->link=first;
				ptr->head=temp;
			}
			while(first!=NULL&&temp->data<first->data){
				prev=first;
				first=first->link;
			}
			prev->link=temp;
			temp->link=first;
		}
		else{
			printf("Invalid choice");
			return;
		}
	}
}


//menu driven part of program to work with linked lists

int main(){
	LLIST myList,revList,myList2; //creates a list myList of LList type
	init(&myList); //initialises myList
	int choice,ele;
	for(;;){
		printf("Enter your choice\n");
		printf("1.Insert at front\n2.Insert at rear\n3.Delete at front\n4.Delete at rear\n5.Display\n6.Search\n7.Count nodes\n8.Reverse list\n9.Insert at a particular position\n10.Create an ordered list\n11.Merge another list\n12.Delete alternate\n13.Exit\n");
        //Accepts choice from user for what operation to conduct
        scanf("%d",&choice);
		switch(choice){
			case 1: printf("Enter the element\n");
					scanf("%d",&ele);
					insert_front(&myList,ele);
                    printf("Element was successfully inserted\n");
					break;
			case 2: printf("Enter the element\n");
					scanf("%d",&ele);
					insert_rear(&myList,ele);
                    printf("Element was successfully inserted\n");
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
						printf("The list is empty\n");
					}
					else{
						printf("Deleted element is %d\n",x);
					}
					break;
			case 5: printf("The list is:\n");
                    display(&myList);
					break;
			case 6: printf("Enter element to search for");
					scanf("%d",&ele);
					int ret=search_list(&myList,ele);
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
			case 7: x=count_node(&myList);
                    if(x==9999){
                        printf("The list is empty\n");
                    }
                    else{
                        printf("The list has %d node(s)\n",x);
                    }
                    break;
            case 8: //init(&revList);
                    x=reverse_list(&myList);
                    if(x==9999){
                        printf("The list is empty\n");
                    }
                    else{
                        printf("The reversed list is\n");
                        display(&myList);
                    }
                    printf("\n\n");
                    break;
            case 9: int pos;
                    printf("Enter the element to insert and what position to insert at\n");
                    scanf("%d %d",&ele,&pos);
                    insert_between(&myList,pos,ele);
                    printf("The element was successfully inserted\n");
                    break;
			case 10:int ord,no;
					printf("Select the ordering method:\n1.Ascending\n2.Descending\n");
					scanf("%d",&ord);
					printf("Enter the number of nodes in the list\n");
					scanf("%d",&no);
					for(int i=0;i<no;i++){
						printf("Enter the element to insert\n");
						scanf("%d",&ele);
						order(&myList,ele,ord);
					}
					printf("\n");
					break;
			case 11:int ele_no,ele,c,i=0;
					init(&myList2);
					printf("How many elements do you want in the other list?\n");
					scanf("%d",&ele_no);
					if(ele_no==0){
						printf("The merged list is:\n");
						display(&myList);
						printf("\n\n");
					}
					else{
						printf("Enter the elements in order\n");
						for(i;i<ele_no;i++){
							printf("Enter the element\n");
							scanf("%d",&ele);
							insert_rear(&myList2,ele);
						}
						merge_list(&myList,&myList2);
						printf("The merged list is:\n");
						display(&myList);
						printf("\n");
					}
					break;
			case 12:delete_alternate(&myList);
					break;
            case 13: exit(0);
		}
	}
    return 0;
}
