# Swap kth elements
# Given an array of size N, swap the kth element from beginning with kth element from end.
'''
 Example:
Input       
1
8 3
1 2 3 4 5 6 7 8
Output
1 2 6 4 5 3 7 8               //8-3=5
 '''

 #--------------------------custom code --------------------------------------
T=int(input("Enter Test case: "))
for i in range(T):
    array=[]
    n=int(input("Enter the size of Array: "))
    x=int(input("Enter the element you want to swap: "))
    print("Enter Array Elemnt: ")
    for i in range(n):
        A=int(input())
        array.append(A)
    array[x-1],array[n-x]=array[n-x],array[x-1]
    print(array)
    


#-------------------------------GFG code-----------------------------------------
# t=int(input())
# for i in range(t):
#     n,x=map(int,input().split())
#     A=list(map(int,input().split()))
#     A[x-1],A[n-x]=A[n-x],A[x-1]
#     for i in range(len(A)):
#         print(A[i],end=" ")

#------------------------------GFG second way-----------------------------------------
# t=int(input())
# for i in range(t):
#     n,x=map(int,input().split())
#     A=input().split()
#     A[x-1],A[n-x]=A[n-x],A[x-1]
#     s = ''
#     s = ' '.join(A)
#     print(s)