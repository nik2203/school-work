#include<stdio.h>
#define MAX 50
void create(int *a, int ele)
{
    int i=0;
    while(i<MAX && a[i]!=0)
    {
        if(ele<a[i])
            i=2*i+1;
        else
            i=2*i+2;
    }
    a[i]=ele;
}

void inorder(int *a, int i)
{
    if(a[i]==0)
        return;
    inorder(a,2*i+1);
    printf("%d",a[i]);
    inorder(a,2*i+2);
    
}

void postorder(int *a, int i)
{
    if(a[i]==0)
        return;
    postorder(a,2*i+1);
    postorder(a,2*i+2);
    printf("%d",a[i]);
}

void preorder(int *a, int i)
{
    if(a[i]==0)
        return;
    printf("%d",a[i]);
    preorder(a,2*i+1);
    preorder(a,2*i+2);
}

int main()
{
    int a[MAX],ele;
    int ch;
    while(1)
    {
        printf(" 1. Create BST\n 2. inorder\n 3. postorder\n 4. preorder\n");
        printf("Enter your choice\n");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1: printf("Enter element\n");
            scanf("%d",&ele);
            create(a, ele);
            break;
            case 2: inorder(a,0);
            break;
            case 3: postorder(a,0);
            break;
            case 4: preorder(a,0);
            break;
        }
    }
}