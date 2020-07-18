# Check if an array is sorted
# Given an array C[], write a program that prints 1 if array is sorted in non-decreasing order, else prints 0.
'''
Example:
Input
2
5
10 20 30 40 50
6
90 80 100 70 40 30

Output
1
0
'''
#-------------------------custom code----------------------------------------
t=int(input("Enter Test Cases: "))
for i in range(t):
    A=[]
    N=int(input("Enter The Size of Array: "))
    print("Enter Array Elemnt: ")
    for i in range(N):
        a=int(input())
        A.append(a)
    print(A)
    sortedarray=sorted(A)
    if A==sortedarray:
        print(1)
    else:
        print(0)


#-----------------------------second method custom code--------------------------

# t=int(input("Enter Test Cases: "))
# for i in range(t):
#     A=[]
#     N=int(input("Enter The Size of Array: "))
#     print("Enter Array Elemnt: ")
#     for i in range(N):
#         a=int(input())
#         A.append(a)
#     print(A)
#     A1=A[:]
#     A1.sort()
#     if A1==A:
#         print(1)
#     else:
#         print(0)

#---------------------------------------GFG code------------------------
# t=int(input())
# for i in range(t):
#     n=int(input())
#     A=list(map(int,input().split()))
#     sorted_array=sorted(A)
#     if A==sorted_array:
#         print(1)
#     else:
#         print(0)