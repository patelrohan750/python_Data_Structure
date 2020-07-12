# At least two greater elements
# Given an array of N distinct elements, the task is to find all elements in array except two greatest elements.
'''
Example:
Input:
2
5
2 8 7 1 5
6
7 -2 3 4 9 -1

Output:
1 2 5
-2 -1 3 4

Explanation:
Testcase 1: Largest two elements are 7 and 8. So array left is 1 2 5.
'''
#--------------------------------------------custom code-------------------------------
t=int(input("Enter test cases: "))
for i in range(t):
    array=[]
    n=int(input("Enter the Size of Array: "))
    print("Enter Array elment: ")
    for i in range(n):
        a=int(input())
        array.append(a)
    array.sort()
    for j in range(0,len(array)-2):
        print(array[j],end=" ")
    print(" ")
#--------------------------------------------GFG code---------------------------------
# t=int(input())
# for i in range(t):
#     n=int(input())
#     A=list(map(int,input().split()))
#     A.sort()
#     for i in range(0,len(A)-2):
#         print(A[i],end=" ")
#     print(" ")
   