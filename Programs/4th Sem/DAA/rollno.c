#include <stdio.h>
#include <stdlib.h>
  

void solution (int rollnumber[],int n){
	int temp;
    for(int i=0;i<n-1;i++){
        for(int j=0;j<n-i-1;j++){
            if(rollnumber[j]>rollnumber[j+1]){
                temp = rollnumber[j];
                rollnumber[j] = rollnumber[j+1];
                rollnumber[j+1] = temp;
            }
        }
    }
    for(int i = 0;i<n;i++){
        printf("%d\t",rollnumber[i]);
    }
	
}
  
int main()
{
     // Driver code
	int n;
	scanf("%d",&n);
	int arr[n];
	for(int i=0;i<n;i++){
		
		scanf("%d",&arr[i]);
		
	}
    
    solution(arr,n);
  
    return 0;
}
