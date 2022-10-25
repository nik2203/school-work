#include "dll.h"
#include <stdio.h>
#include <stdlib.h>
 
list_t* create_list()  // return a newly created empty doubly linked list
{
	// DO NOT MODIFY!!!
	list_t* l = (list_t*) malloc(sizeof(list_t)); // This is dynamically allocating memory that is used to create a list 
	l->head = NULL;
	l->tail = NULL;
	l->size = 0;
	return l;
}

void insert_front(list_t* list, int data)  // TODO: inserts data to the beginning of the linked list
{
	node_t* temp = (node_t*)malloc(sizeof(node_t)); //temporary node that stores data value to be inserted
	temp->data=data; 		// Storing the data in the created temporary node
	temp->prev=temp->next=NULL; // Making both the prev and next pointers of that node NULL 
	if(list->head==NULL){    // Checking if the list is empty 
		list->head=list->tail=temp;
	}
	else{
		node_t *first=list->head; // Represents the first node of the empty list
		first->prev=temp; 
		temp->next=first;
		list->head=temp;
	}
	list->size++; // Increasing the size after the node has been added 
}

void insert_back(list_t* list, int data) // TODO: inserts data to the end of the linked list
{
	node_t* temp = (node_t*)malloc(sizeof(node_t)); //temporary node that stores data value to be inserted
	temp->data=data; // Storing the data in the created temporary node
	temp->prev=temp->next=NULL; // Making both the prev and next pointers of that node NULL 
	if(list->head==list->tail){ // Checking if the list is empty 
		insert_front(list,data);
	}
	else{
		node_t *last=list->tail; // Denotes the last node in the list
		last->next=temp;
		temp->prev=last;
		list->tail=temp;
	}
	list->size++; //Increasing the size after the node has been added 
}

void insert_after(list_t* list, int data, int prev) // TODO: inserts data after the node with data “prev”. Do not insert or do anything if prev doesn't exist
{
	node_t* temp = (node_t*)malloc(sizeof(node_t)); //temporary node that stores data value to be inserted
	temp->data=data; // Storing the data in the created temporary node
	temp->prev=temp->next=NULL; // Making both the prev and next pointers of that node NULL 
	if(list->head==NULL){
		return;
	}
	else{
		node_t* cur=list->head; // creating a pointer that points to the first node
		while(cur->data!=prev && cur->next!=NULL){
			cur=cur->next;
		}
		if(cur->data==prev && cur->next!=NULL){
			node_t* next=cur->next;
			temp->next=next;
			cur->next=temp;
			temp->prev=cur;
			next->prev=temp;
			list->size++;
		}
		else if(cur->data==prev && cur->next==NULL){
			cur->next=temp;
			temp->prev=cur;
			list->size++;
		}
		else{
			return;
		}
	}
}

void delete_front(list_t* list) // TODO: delete the start node from the linked list.
{
	if(list->size==0){
		return;
	}
	else{
		node_t* first=list->head;
		node_t* second=first->next;
		if(second==NULL){	// Checking if the list has only 1 node and then freeing the first node
			list->head=list->tail=NULL;
			free(first);
			first=NULL;
		}
		else{
			list->head=second;
			second->prev=NULL;
			free(first);
		}
	}
	list->size--;
}

void delete_back(list_t* list) // TODO: delete the end node from the linked list.
{
	node_t* cur=list->head;
	if(list->head==NULL){
		return;
	}
	else if(list->size==1){ // checking if the list has 1 node i.e the first node and then freeing it
		free(cur);
		list->head=list->tail=NULL; 
	}
	else{
		node_t* last=list->tail; // Making two new nodes that denote the last and last second nodes
		node_t* newlast=last->prev;
		newlast->next=NULL;
		list->tail=newlast;
		free(last);
		list->size--;
	}
}

void delete_node(list_t* list, int data) // TODO: delete the node with “data” from the linked list.
{
	if(list->size==0){
		return;
	}
	else{
		node_t* delnode=search(list,data); // calling the search function which returns the pointer pointing to that node in the list
		if(delnode==NULL){
			return;
		}
		else{
			if(delnode->prev==NULL){ // checking if it's the first node and then calling the deletefront function
				delete_front(list);
			}
			else if(delnode->next==NULL){
				delete_back(list); // checking if it's the last node and calling the deleteback function
			}
			else{
				node_t* prev = delnode->prev; // making a new node that denotes the prev node of the node to be deleted
				prev->next=delnode->next;
				delnode->next->prev=prev;
				free(delnode); 
			}
		}
	}
}

node_t* search(list_t* list, int data) // TODO: returns the pointer to the node with “data” field. Return NULL if not found.
{
	if(list->size==0){
		return NULL;
	}
	else{
		node_t* cur=list->head; // making pointer that points to the first node and then keep going next until the data is found.
		while(cur!=NULL){
			if(cur->data==data){
				return cur; // returns the pointer pointing to the data 
			}
			cur=cur->next;
		}
		return NULL;
	}
}

int is_empty(list_t* list) // return true or 1 if the list is empty; else returns false or 0
{
	// DO NOT MODIFY!!!
	return list->size == 0;
}

int size(list_t* list) // returns the number of nodes in the linked list.  
{
	// DO NOT MODIFY!!!
	return list->size;
}

void delete_nodes(node_t* head) // helper
{
	// DO NOT MODIFY!!!
	if(head == NULL)
		return;
	delete_nodes(head->next);
	free(head);	
}

void delete_list(list_t* list) // free all the contents of the linked list
{
	// DO NOT MODIFY!!!
	delete_nodes(list->head);
	free(list);
}

void display_list(list_t* list) // print the linked list by separating each item by a space and a new line at the end of the linked list.
{
	// DO NOT MODIFY!!!
	node_t* it = list->head;
	while(it != NULL)
	{
		printf("%d ", it->data);
		it = it->next;
	}
	printf("\n");
}

