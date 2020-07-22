# Form largest number from digits
# Given an array of numbers form 0 to 9 of size N. Your task is to rearrange elements of the array such that after combining all the elements of the array number formed is maximum
'''
Example:
Input:
2
5
9 0 1 3 0
3
1 2 3

Output:
93100
321

Explanation:
Testcase1: Largest number is 93100 which can be formed from array digits.
'''
#----------------------------custom code-------------------------------
t=int(input("Enter Test Cases: "))
for i in range(t):
    A=[]
    maxA=[]
    n=int(input("Enter size of the array: "))
    print("Enter Elemnt: ")
    for i in range(n):
        a=int(input())
        A.append(a)
    print(A)
    A.sort()
    print(A)
    rev=A[::-1]
    print(rev)
    for i in range(len(rev)):
        print(rev[i],end="")


#----------------------------------GFG code---------------------------
# t=int(input())
# for i in range(t):
#     n=int(input())
#     A=list(map(int,input().split()))
#     A.sort()
#     rev=A[::-1]
#     for i in range(len(rev)):
#         print(rev[i],end="")
#     print()