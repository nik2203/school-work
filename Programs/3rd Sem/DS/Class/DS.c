#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<ctype.h>

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
}