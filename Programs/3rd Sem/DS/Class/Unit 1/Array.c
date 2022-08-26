#include<stdio.h>
#include<stdlib.h>


//macros

#define MAX 3


//structures

typedef struct array{
	int *a;
	int size;
	int used_size;
}ALIST;


//functions

void init(ALIST *ptr){
	ptr->size=0;
	ptr->used_size=-1;
}

void alloc(ALIST *ptr){
	if(ptr->size==0){
		ptr->a=(int*)malloc(MAX*sizeof(int));
		ptr->size=MAX;
	}
	else if(ptr->used_size==MAX-1){
		ptr->a=(int*)realloc(ptr->a,2*ptr->size*sizeof(int));
		ptr->size=2*ptr->size;
	}
}

void insert(ALIST *ptr,int ele){
	alloc(ptr);
	ptr->used_size++;
	ptr->a[ptr->used_size]=ele;
}

int delete(ALIST *ptr){
	if(ptr->used_size==-1){
		return 9999;
	}
	int x=ptr->a[ptr->used_size];
	ptr->used_size--;
	return x;
}

void display(ALIST *ptr){
	if(ptr->used_size==-1){
		printf("List is empty\n");
		return;
	}
	printf("The array is:\n");
	for(int i=0;i<=ptr->used_size;i++){
		printf("%d\t",ptr->a[i]);
	}
	printf("\n");
}

int main(){
	ALIST list;
	init(&list);
	int choice,ele,x;
	while(1){
		printf("Enter your choice\n");
		printf("1.Insert an element\n2.Delete an element\n3.Display\n4.Exit\n");
		scanf("%d",&choice);
		switch(choice){
			case 1: printf("Enter the element to insert\n");
					scanf("%d",&ele);
					insert(&list,ele);
					break;
			case 2: x=delete(&list);
					if(x==9999){
						printf("The list is empty\n");
					}
					else{
						printf("The deleted element is %d\n",x);
					}
					break;
			case 3: display(&list);
					break;
			case 4: exit(0);
		}
	}
	return 0;
}