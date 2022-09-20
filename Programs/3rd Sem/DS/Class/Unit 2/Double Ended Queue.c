#include<stdio.h>
#include<stdlib.h>

#define MAX 100

//node structure
typedef struct node{
	int data;
	struct node* link;
}NODE;

//circular queue structure with pointers to front and rear nodes
typedef struct cq{
	NODE *f,*r;
}CQ;

int main(){
	//dynamically allocate memory for circular queue
	CQ *ptr=malloc(sizeof(CQ));
	ptr->f=ptr->r=NULL; //initialise the front and rear node pointers to point to null as queue is empty
	int choice,choice1,ele,x;
	while(1){
		printf("Enter your choice\n");
		printf("1.Input Restricted\n2.Output Restricted\n3.Exitn");
		scanf("%d",&choice);
        if(choice==1){
            printf("Enter your choice\n");
            printf("1.Insert at the rear\n2.Delete from the front\n3.Delete from the rear\n");
            scanf("%d",choice1);
            switch (choice1){
            case 1: break;
            case 2: break;
            case 3: break;
            }
        }
        else if(choice==2){
            printf("Enter your choice\n");
            printf("1.Insert at the front\n2.Insert at the front\n3.Delete from the rear\n");
            scanf("%d",choice1);
            switch (choice1){
            case 1: break;
            case 2: break;
            case 3: break;
            }
        }
        else if(choice==3){
            exit(0);
        }
        else{
            printf("Inavlid input");
        }
	}
	return 0;
}