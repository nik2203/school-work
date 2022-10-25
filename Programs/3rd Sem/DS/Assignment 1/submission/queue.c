#include "queue.h"
#include <stdio.h>
#include <stdlib.h>

queue_t* create_queue()   // return a newly created empty queue
{
	// DO NOT MODIFY!!!
	queue_t* Q = (queue_t*) malloc(sizeof(queue_t));
	Q->list = create_list();
	Q->front = Q->list->head;
	Q->rear = Q->list->tail;
	Q->size = Q->list->size;
	return Q;
}

void enqueue(queue_t* q, int data) // TODO: insert data at the end of a queue
{
	node_t* temp = (node_t*)malloc(sizeof(node_t)); // Creating a temporary node and dynamically assigning memory
	temp->data=data;
	if(q->size==0){
		q->front=q->rear=temp;
		temp->prev=q->front;
	}
	else{
		node_t* last=q->rear;
		last->next=temp;
		temp->prev=last;
		q->rear=q->rear->next;
	}
	q->size++;
}

int dequeue(queue_t* q) 	// TODO: return the data at the front of a queue and remove it. Return -1 if queue is empty
{
	int x;
	if(q->size==0){
		return -1;
	}
	else if(q->size==1){ // checking is the queue contains only one element and then freeing the first element
		node_t* first=q->front;
		x=first->data;
		free(first);
		q->front=NULL;
		q->size--;
		return x;
	}
	else{
		node_t* first=q->front;
		node_t* second=first->next; // As we know that queue follows First in First out so when dequeing the first elemtn should be deleted. 
		x=first->data;
		second->prev=NULL;
		q->front=second;
		free(first); // as the second node becomes the first node making the prev pointer pointing to NULL
		q->size--;
		return x;
	}
}

int front(queue_t* q) // TODO: return the data at the front of a queue. Return -1 if queue is empty
{
	if(q->size==0){
		return -1;
	}
	else{
		int x=q->front->data; // Returns the first element
		return x;
	}
}

int empty(queue_t* q) // return if the queue is empty
{
	// DO NOT MODIFY!!!
	return is_empty(q->list);
}

int queue_size(queue_t* q) // returns the number of elements in the queue
{
	// DO NOT MODIFY!!!
	return q->size;
}

void delete_queue(queue_t* q) // empty the contents of the queue
{
	// DO NOT MODIFY!!!
	delete_list(q->list);
	free(q);
}
