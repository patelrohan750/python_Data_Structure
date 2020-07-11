# Calculate the product of all the elements in an array.
'''
Example:
Input:
2
5
1 2 3 4 5
10
5 5 5 5 5 5 5 5 5 5

Output:
120
9765625
'''
#--------------------------custom code ----------------------------
t=int(input("Enter test cases: "))
for i in range(t):
    list1=[]
    mul=1
    n=int(input("enter the size of array: "))
    print("enter array element: ")
    for i in range(n):
        a=int(input())
        list1.append(a)
    print(list1)
    for i in range(n):
        mul *=list1[i]
    print(mul)





#--------------------------------GFG code---------------------------------
#code
# t=int(input())
# for i in range(t):
#     mul=1
#     n=int(input())
#     A=list(map(int,input().split()))
#     for i in range(n):
#         mul *=A[i]
#     print(mul)
        
