// Program to add two polynomials that are stored as linked lists


#include<stdio.h>
#include<stdlib.h>

typedef struct poly{
    int coeff;
    int px;
    int py;
    struct poly* link;
}NODE;

typedef struct plist{
    NODE * head;
}LIST;

void init(LIST *ptr){
    ptr->head=NULL;
}

NODE* create_node(int coeff,int px,int py){
    NODE *temp;
    temp=(NODE*)malloc(sizeof(NODE));
    if(temp!=NULL){
        temp->coeff=coeff;
        temp->px=px;
        temp->py=py;
    }
    return(temp);
}

void insert(LIST *ptr,int ele,int px,int py){
    NODE *temp;
    temp=create_node(ele,px,py);
    NODE *cur=ptr->head;
    if(ptr->head==NULL){
        ptr->head=temp;
        temp->link=NULL;
    }
    else{
        while(cur->link!=NULL){
            cur=cur->link;
        }
        temp->link=NULL;
        cur->link=temp;
    }
}

void display(LIST *ptr){
    NODE *cur=ptr->head;
    if(ptr->head==NULL){
        printf("The polynomial does not exist\n");
    }
    else{
        printf("The polynomial is:\n");
        while(cur->link!=NULL){
            printf("%dx^%dy^%d + ",cur->coeff,cur->px,cur->py);
            cur=cur->link;
        }
        printf("%dx^%dy^%d\n",cur->coeff,cur->px,cur->py);
    }
}

void add_poly(LIST *ptr1,LIST *ptr2,LIST *ptr3){
    NODE *cur1=ptr1->head;
    NODE *cur2=ptr2->head;
    NODE *cur3=ptr3->head;
    int flag=0,coeff,px,py;
    while(cur1!=NULL){
        flag=0;
        cur2=ptr2->head;
        coeff=cur1->coeff;
        px=cur1->px;
        py=cur1->py;
        while(cur2!=NULL){
            if((cur1->px==cur2->px)&&(cur1->py==cur2->py)){
                coeff+=cur2->coeff;
            }
            cur2=cur2->link;
        }
        insert(ptr3,coeff,px,py);
        cur1=cur1->link;
    }
    cur1=ptr1->head;
    cur2=ptr2->head;
    while(cur2!=NULL){
        flag=0;
        cur1=ptr1->head;
        cur3=ptr3->head;
        while(cur3!=NULL && flag==0){
            if((cur2->px==cur3->px)&&(cur2->py==cur1->py)){
                flag++;
            }
            while(cur1!=NULL){
                if((cur2->px==cur1->px)&&(cur2->py==cur1->py)){
                    flag++;
                }
                cur1=cur1->link;
            }
            cur3=cur3->link;
        }
        if(flag==0){
            insert(ptr3,cur2->coeff,cur2->px,cur2->py);
        }
        cur2=cur2->link;
    }    
}

int main(){
    LIST poly1,poly2,polysum;
    init(&poly1);
    init(&poly2);
    init(&polysum);
    int choice,ele,px,py,i,no;
    for(;;){
        printf("Enter your choice\n");
        printf("1.Add two polynomials\n2.View a polynomial\n3.Exit\n");
        scanf("%d",&choice);
        switch(choice){
            case 1: printf("Enter the amount of elements of polynomial 1\n");
                    scanf("%d",&no);
                    for(i=0;i<no;i++){
                        printf("Enter the coefficient, power of x, and power of y\n");
                        scanf("%d %d %d",&ele,&px,&py);
                        insert(&poly1,ele,px,py);
                        printf("The node was successfully inserted\n");
                    }
                    printf("Enter the amount of elements of polynomial 2\n");
                    scanf("%d",&no);
                    for(i=0;i<no;i++){
                        printf("Enter the coefficient, power of x, and power of y\n");
                        scanf("%d %d %d",&ele,&px,&py);
                        insert(&poly2,ele,px,py);
                        printf("The node was successfully inserted\n");
                    }
                    add_poly(&poly1,&poly2,&polysum);
                    break;
            case 2: printf("Do you want to view polynomial 1, 2 or 3\n");
                    scanf("%d",&no);
                    if(no==1){
                        display(&poly1);
                    }
                    else if(no==2){
                        display(&poly2);
                    }
                    else if(no==3){
                        display(&polysum);
                    }
                    else{
                        printf("Invalid input\n");
                    }
                    break;
            case 3: exit(0);
        }
    }
    return 0;
}