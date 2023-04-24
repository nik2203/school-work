/*  
0 10 0 5 0
0 0 1 2 0 
0 0 0 0 4
0 3 9 0 2
20 0 6 0 0 

*/

#include<stdio.h>
int g[100][100] ,inf =9999 ,min ,mincost=0 ,visted[10];
int prism(int n)
{
	int j,i,k,v1,v2;
	for(j=1; j<=n;j++)
	{
		visted[j]=0;
	}
	visted[1]=1;
	for(k=1; k<n; k++)
	{
		min=inf;
	    for(i=1; i<=n; i++)
	    {
	    	for(j=1; j<=n; j++)
	    	{
	    		if(g[i][j]!=inf && visted[i]==1 && visted[j]==0)
	    		{
	    			if(g[i][j]<min)
	    			{
	    				min=g[i][j];
	    				v1=i;
	    				v2=j;
					}
				}
			}
			
		}
		printf("edge:->%d=(%d-->%d)\n",k,v1,v2);
		visted[v1]=visted[v2]=1;
		mincost=mincost+min;
	}
	printf("mincost %d",mincost);
}


int main()
{
	int i,n,j;
	printf("enter the vertex\n");
	scanf("%d",&n);
	for(int i=1; i<=n; i++)
	{
		for(int j=1; j<=n; j++)
		{
			scanf("%d",&g[i][j]);
			if(g[i][j]==0)
			g[i][j]=inf;
		}
	}
	prism(n);
}
