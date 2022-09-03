//Stack

#include<stdio.h>
#include<stdlib.h>

#define MAX 5

typedef struct stack{
	int top;
	int a[MAX];
}STACK;

void push(STACK *ptr, int ele){
	if(ptr->top==MAX-1){
		printf("Overflow condition\n");
	}
	else{
		ptr->a[++ptr->top]=ele;
		printf("Successfully pushed\n");
	}
}

int pop(STACK *ptr){
	if(ptr->top==-1){
		return 9999;
	}
	else{
		int x=ptr->a[ptr->top];
		ptr->top--;
		return x;
	}
}

void display(STACK *ptr){
	if(ptr->top==-1){
		printf("The stack is empty");
	}
	else{
		printf("The stack is:\n");
		for(int i=0;i<ptr->top+1;i++){
			printf("%d\t",ptr->a[i]);
		}
	}
	printf("\n");
}

void peep(STACK *ptr){
	if(ptr->top==-1){
		printf("The stack is empty\n");
	}
	else{
		printf("The top element is %d\n",ptr->a[ptr->top]);
	}
}


int main(){
	STACK *ptr = NULL, s;
	ptr=&s;
	s.top=-1;
	int choice,ele,x;
	while(1){
		printf("Enter your choice\n");
		printf("1.Push\n2.Pop\n3.Display\n4.Peep\n5.Exit\n");
        //Accepts choice from user for what operation to conduct
        scanf("%d",&choice);
		switch(choice){
			case 1: printf("Enter element to push\n");
					scanf("%d",&ele);
					push(ptr,ele);
					break;
			case 2: x=pop(ptr);
					if(x=9999){
						printf("Underflow condition\n");
					}
					else{
						printf("The popped value is %d\n",x);
					}
					break;
			case 3:	display(ptr);
					break;
			case 4: peep(ptr);
					break;
			case 5: exit(0);
		}
	}
	return 0;
}