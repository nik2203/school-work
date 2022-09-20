#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include <math.h>

//macro to define max size of expression
#define MAX 100

//stack structure
typedef struct stack{
	int top;
    char st[MAX];
}STACK;

//push operation to add an element to the stack
void push(STACK *ptr, char ele){
    ptr->top++;
    ptr->st[ptr->top]=ele;
}

//pop operation to remove an element from the stack
char pop(STACK *ptr){
    return ptr->st[ptr->top--];
}

//used to ascertain priority of operators during evaluation
int priority(char ele){
    switch(ele){
        case '+':
        case '-': return 1;
        case '*':
        case '/': 
        case '%': return 2;
        case '^':
        case '$': return 3;
        default: return 0;
    }
}

//upon scanning an operator, conducts the operation associated with it
int compute(char symbol, int op1, int op2){
    switch(symbol){
        case '+': return (op1 + op2);
        case '-': return (op1 - op2);
        case '*': return (op1 * op2);
        case '/': return (op1 / op2);
        case '%': return (op1 % op2);
        case '$':
        case '^': return (pow(op1, op2));
    }
}

int main(){

    char inf[MAX], infix[MAX], prefix[MAX]; //defining the strings for initial infix, reversed infix and prefix expressions
    int len,j=0;
    STACK *ptr,s; //defines a stack and a pointer to the stack
    s.top=-1;
    ptr=&s;

    scanf("%d %s", &len,inf); //accepts input of length of expression and expression itself
    push(ptr,'('); //adds an initial bracket to the expression
    int i=0,sum=0;
    int maxl=len-1;

    while(maxl>=0){ //contents of the while loop reverse the initial infix expression including brackets
        if(inf[maxl]=='('){
            infix[i]=')';
		}
        else if(inf[maxl]==')'){
            infix[i]='(';
		}
        else{
            infix[i]=inf[maxl];
            sum++;
        }
        maxl--;
        i++;
    }
    len=sum;
    strcat(infix,")"); //appends a closing bracket to the expression

	//body of the infix to postfix function has been placed into the main body as it was not working when inside the function
    char x;
    i=0;
    while(infix[i]!='\0'){ //while loop condition checks to make sure the end of string is not reached
        if(infix[i]=='('){
            push(ptr,infix[i]);
        } //brackets are pushed into the stack
        else if(isalnum(infix[i])){
            prefix[j++]=infix[i];
        } //alphanumeric characters are added to the prefix expression
        else if(infix[i]==')'){
            while(s.st[s.top]!='('){
                prefix[j++]=pop(ptr); //if a closing bracket is encountered, all elements in stack are popped into the prefix expression until an opening bracket is encountered
            }
            x=pop(ptr);
        }
        else{
            while(priority(s.st[s.top])>priority(infix[i])){ //if an operator is encountered, elements in stack are popped to the prefix expressions until an element of lesser priority is encountered
                prefix[j++]=pop(ptr);
            }
            push(ptr,infix[i]);
        }
        i++;
    }
    prefix[j]='\0';

    i=len-1;
    while(i>=0){
        printf("%c",prefix[i]);
        i--; //as the expression obtained from the code above is the postfix of the reversed expression, we must reverse it once more to obtain the prefix expression for the initial infix expression
    }


    int st[100], top=-1;
    int res, op1, op2;
    char symbol;
    for (i=0;i<len;i++){
        symbol=prefix[i];
        if (isdigit(symbol)){
            st[++top]=(int)(symbol - '0'); //if the scanned symbol is a number it is added to the stack
        }
        else{ //if the scanned symbol is an operator, a computation of value occurs
            op1=st[top--];
            op2=st[top--];
            res=compute(symbol, op1, op2);
            st[++top]=res;
        }
    }
    res=st[top];
    printf(" %d",res); //prints the evaluated result of the prefix expression
    return 0;
}