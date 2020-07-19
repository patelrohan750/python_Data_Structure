# Print the left element
# Given a array of length N, at each step it is reduced by 1 element. In the first step the maximum element would be removed, while in the second step minimum element of the remaining array would be removed, in the third step again the maximum and so on. Continue this till the array contains only 1 element. And print that final element remaining in the array.
'''
Example:
Input:
2
7
7 8 3 4 2 9 5
8
8 1 2 9 4 3 7 5

Ouput:
5
4

Explanation:
Test Case 1:
In first step '9' would be removed, in 2nd step '2' will be removed, in third step '8' will be removed and so on. So the last remaining element would be '5'.   
'''

#----------------------------------custom code---------------
# t=int(input("Enter The Test Cases: "))
# for i in range(t):
#     A=[]
#     n=int(input("Enter the size of arrray: "))
#     print("Enter Array Elements: ")
#     for i in range(n):
#         a=int(input())
#         A.append(a)
#     print(A)
#     for i in A:
#         max_ele=max(A)
#         # print(max_ele)
#         A.remove(max_ele)
#         min_ele=min(A)
#         # print(min_ele)
#         A.remove(min_ele)
#     print(A)
#---------------------------second way custom code--------------------
t=int(input("Enter The Test Cases: "))
for i in range(t):
    A=[]
    n=int(input("Enter the size of arrray: "))
    print("Enter Array Elements: ")
    for i in range(n):
        a=int(input())
        A.append(a)
    print(A)
    A.sort()
    print(A)
    print(A[(n-1)//2])
#-------------------------------GFG code------------------------------
#code
# t=int(input())
# for i in range(t):
#     n=int(input())
#     A=list(map(int,input().split()))
#     A.sort()
#     print(A[(n-1)//2])
