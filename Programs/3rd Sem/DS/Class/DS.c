#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<ctype.h>
#define MAX 5

void enque(){
}

int dequeue(){
	
}

int main(){
	int q[MAX],f=0,r=-1;
	int choice,ele; 
	while(1){
		printf("1.Enque\n2.Deque\n3.Display\n4.Exit\n");
		printf("Enter your choice\n");
		scanf("%d",&choice);
		switch(choice){

		}
	}
}


/*
typedef struct stack{
	char arr[MAX];
	int top;
}STACK;

void push(STACK *ptr, char ele){
	ptr->top++;
	ptr->arr[ptr->top]=ele;
}

void pop(STACK *ptr){
	ptr->top--;
}


int main(){
	STACK *ptr,st;
	st.top=-1;
	ptr=&st;
	char exp[MAX];
	printf("Enter an expression \n");
	scanf("%s",expr);
	int i=0;
	while(expr[i]!='\0'){
		if(expr[i]=='('||expr[i]=='{'||expr[i]=='['){
			push(ptr,exp[i]);
		}
		else if(expr[i]=='('||expr[i]=='{'||expr[i]=='['){
			if(expr[i]==')' && ptr->arr[ptr->top]=='('){
				pop(ptr);
			}
			else if(expr[i]=='}' && ptr->arr[ptr->top]=='{'){
				pop(ptr);
				else if(expr[i]==']' && ptr->arr[ptr->top]=='['){
				pop(ptr);
			}
			else{
				printf("unbalanced expression\n");
			}
		}
	}
}


int compute(char symb,int op1,int op2){
	switch(symb){
		case '+': return(op1+op2);
		case '-': return(op1-op2);
		case '*': return(op1*op2);
		case '%': return(op1%op2);
		case '$':
		case '^': return(pow(op1,op2));
	}
}


int main(){
	char postfix[100];
	int i,s[100],top=-1;
	int res,op1,op2;
	char symb;
	printf("Enter the postfix expression\n");
	scanf("%s",postfix);
	for(i=0;i<strlen(postfix);i++){
		symb=postfix[i];
		if(isdigit(symb)){
			s[++top]=symb;
		}
		else{
			op2=s[top--];
			op1=s[top--];
			res=compute(symb,op1,op2);
		}
		res=s[top--];
		printf("%d\n",res);
	}
	return 0;
}*/