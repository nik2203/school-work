l=[1,3,23,7,8,4,5]
for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
        else:
            continue
print(l)
l=[1,3,2,4,5]
for i in range(1,len(l)):
    key=l[i]
    j=i-1
    while j>=0 and key<l[j]:
        l[j+1]=l[j]
        j=j-1

    else:
        l[j+1]=key
    print(l)

print(l)

# Python program for implementation of Selection 
# Sort 
A = [64, 25, 12, 22, 11] 

# Traverse through all array elements 
for i in range(len(A)): 
	
	# Find the minimum element in remaining 
	# unsorted array 
	min_idx = i 
	for j in range(i+1, len(A)): 
		if A[min_idx] > A[j]: 
			min_idx = j 
			
	# Swap the found minimum element with 
	# the first element		 
	A[i], A[min_idx] = A[min_idx], A[i] 

# Driver code to test above 
print ("Sorted array") 
for i in range(len(A)): 
	print("%d" %A[i]), 

