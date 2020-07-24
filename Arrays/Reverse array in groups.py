#-------------------------------Amzon-------------------------------
# Reverse array in groups
# Given an array arr[] of positive integers of size N. Reverse every sub-array of K group elements.
'''
Input:
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of two lines of input. The first line of each test case consists of an integer N(size of array) and an integer K separated by a space. The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each test case, print the modified array.

Constraints:
1 ≤ T ≤ 200
1 ≤ N, K ≤ 107
1 ≤ A[i] ≤ 1018

Example:
Input
2
5 3
1 2 3 4 5
6 2
10 20 30 40 50 60

Output
3 2 1 5 4
20 10 40 30 60 50

Explanation:
Testcase 1: Reversing groups in size 3, first group consists of elements 1, 2, 3. Reversing this group, we have elements in order as 3, 2, 1.
'''



#----------------------------------------------------custom code---------------------
t=int(input("Enter Test Cases: "))
for i in range(t):
    A=[]
    a1=[]
    n,k=int(input("Enter The size of Array: ")),int(input("Enter The Number which  You want to group: "))
    print("Enter The Array Element: ")
    for i in range(n):
        a=int(input())
        A.append(a)
    print(A)
    for i in range(0,len(A),k):
        a=A[i:i+k]
        rev=a[::-1]
        a1.extend(rev)
    print(a1)
     
    for i in range(len(a1)):
        print(a1[i],end=" ")
    
    
#---------------------------------GFG code-------------------------------------
# t=int(input())
# for i in range(t):
#     rev_array=[]
#     n,k=map(int,input().split())
#     A=list(map(int,input().split()))
#     for i in range(0,len(A),k):
#         a=A[i:i+k]
#         rev=a[::-1]
#         rev_array.extend(rev)
        
#     for i in range(len(rev_array)):
#         print(rev_array[i],end=" ")
#     print()