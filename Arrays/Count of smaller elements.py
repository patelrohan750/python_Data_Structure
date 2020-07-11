# Count of smaller elements
# Given an sorted array A of size N. Find number of elements which are less than or equal to given element X.
'''
Example:
Input:
2
6
1 2 4 5 8 10
9
7
1 2 2 2 5 7 9
2
Output:
5
4
'''

#-------------------------------custom code------------------------------
T=int(input("Enter Test Cases: "))
for i in range(T):
    array=[]
    n=int(input("Enter Size of Array: "))
    print("Enter Array Elemnts: ")
    for i in range(n):
        a=int(input())
        array.append(a)
    print(array)
    x=int(input("Enter Element which check to less than or equal to: "))
    count=0
    for i in range(n):
        if array[i] <=x:
            count+=1
    print(count)
        
#----------------------------------GFG code-----------------------------------
#code
# t=int(input())
# for i in range(t):
#     n=int(input())
#     A=list(map(int,input().split()))
#     x=int(input())
#     count=0
#     for i in range(n):
#         if A[i] <=x:
#             count+=1
#     print(count)
            

