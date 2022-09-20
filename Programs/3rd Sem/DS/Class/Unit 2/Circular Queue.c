#include<stdio.h>
#include<stdlib.h>

#define MAX 5

void enqueue(int q[], int *f, int *r, int ele){
	if((*f==*r+1)||(*f==0&&*r==MAX-1)){
		printf("Overflow condition\n");
	}
	else{
		if(*f==-1){
			*f=0;
		}
		*r=(*r+1)%MAX;
		q[*r]=ele;
	}
}

void display(int q[], int f, int r){
	if(f==-1){
		printf("Underflow condition\n");
		return;
	}	
	for(int i=f;i!=r;i=(i+1)%MAX){
		printf("%d\t",q[i]);
	}
	printf("%d\n",q[r]);
}

int dequeue(int q[], int *f. int *r){
	if(*f==-1){
		return 9999;
	}
	else{
		int x;
		if(*f==*r){
			x=q[f];
			*f=-1;
			*r=-1;
			return x;
		}
		else{
			x=q[*f];
			*f=(*f+1)%MAX;
		}
	}
}

int main(){
	int q[MAX],f=-1;
	int choice,ele;
	while(1){
		printf("Enter your choice\n");
		printf("1.Enqueue\n2.Dequeue\n3.Display\n4.Exit\n");
		scanf("%d",&choice);
		switch(choice){
			case 1: printf("Enter the element\n");
					scanf("%d",&ele);
					enqueue(q[],)
		}
	}
	return 0;
}