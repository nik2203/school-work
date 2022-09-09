#include<stdio.h>
#include<string.h>
#define MAX 100

typedef struct stack
{
    char st[MAX];
    int top;
}STACK;

void push(STACK *ptr, char ele)
{
    ptr->top++;
    ptr->st[ptr->top]=ele;
}

char pop(STACK *ptr)
{
    return ptr->st[ptr->top--];
}

int priority(char ele)
{
    switch(ele)
    {
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

int main()
{
    char infix[MAX], postfix[MAX];
    STACK *ptr,s;
    int k=0;
    s.top=-1;
    ptr=&s;
    printf("Enter a valid infix expression\n");
    scanf("%s",infix);
    push(ptr,'(');
    strcat(infix,")");
    int i=0;
    char x;
    while(infix[i]!='\0')
    {
        if(infix[i]=='(')
            push(ptr,infix[i]);
        else if(isalnum(infix[i]))
            postfix[k++]=infix[i];
        else if(infix[i]==')')
        {
            while(s.st[s.top]!='(')
            {
                postfix[k++]=pop(ptr);
            }
            x=pop(ptr);
        }
        else
        {
            while(priority(s.st[s.top])>=priority(infix[i]))
            {
                postfix[k++]=pop(ptr);
            }
            push(ptr,infix[i]);
        }
        i++;
    }
    postfix[k]='\0';
    puts(postfix);
    return 0;
}