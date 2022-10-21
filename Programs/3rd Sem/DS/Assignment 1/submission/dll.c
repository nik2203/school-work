#include "dll.h"
#include <stdio.h>
#include <stdlib.h>
 
list_t* create_list()  // return a newly created empty doubly linked list
{
	// DO NOT MODIFY!!!
	list_t* l = (list_t*) malloc(sizeof(list_t));
	l->head = NULL;
	l->tail = NULL;
	l->size = 0;
	return l;
}

void insert_front(list_t* list, int data)  // TODO: inserts data to the beginning of the linked list
{
	node_t* temp = (node_t*)malloc(sizeof(node_t)); //temporary node that stores data value to be inserted
	temp->data=data;
	temp->prev=temp->next=NULL;
	if(list->head==NULL){
		list->head=list->tail=temp;
	}
	else{
		node_t *first=list->head;
		first->prev=temp;
		temp->next=first;
		list->head=temp;
	}
	list->size++;
}

void insert_back(list_t* list, int data) // TODO: inserts data to the end of the linked list
{
	node_t* temp = (node_t*)malloc(sizeof(node_t)); //temporary node that stores data value to be inserted
	temp->data=data;
	temp->prev=temp->next=NULL;
	if(list->head==list->tail){
		insert_front(list,data);
	}
	else{
		node_t *last=list->tail;
		last->next=temp;
		temp->prev=last;
		list->tail=temp;
	}
	list->size++;
}

void insert_after(list_t* list, int data, int prev) // TODO: inserts data after the node with data “prev”. Do not insert or do anything if prev doesn't exist
{
	node_t* temp = (node_t*)malloc(sizeof(node_t)); //temporary node that stores data value to be inserted
	temp->data=data;
	temp->prev=temp->next=NULL;
	if(list->head==NULL){
		return;
	}
	else{
		node_t* cur=list->head;
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
		if(second==NULL){
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
	else if(list->size==1){
		free(cur);
		list->head=list->tail=NULL;
	}
	else{
		node_t* last=list->tail;
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
		node_t* delnode=search(list,data);
		if(delnode==NULL){
			return;
		}
		else{
			if(delnode->prev==NULL){
				delete_front(list);
			}
			else if(delnode->next==NULL){
				delete_back(list);
			}
			else{
				node_t* prev = delnode->prev;
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
		node_t* cur=list->head;
		while(cur!=NULL){
			if(cur->data==data){
				return cur;
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

