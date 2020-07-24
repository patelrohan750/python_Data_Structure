#------------------------Amzon,microsoft,snapdeal,hike,Vmware
# Kth smallest element
# Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.
'''
Input:
The first line of input contains an integer T, denoting the number of testcases. Then T test cases follow. Each test case consists of three lines. First line of each testcase contains an integer N denoting size of the array. Second line contains N space separated integer denoting elements of the array. Third line of the test case contains an integer K.

Output:
Corresponding to each test case, print the kth smallest element in a new line.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= arr[i] <= 105
1 <= K <= N

Example:
Input:
2
6
7 10 4 3 20 15
3
5
7 10 4 20 15
4
Output:
7
15

Explanation:
Testcase 1: 3rd smallest element in the given array is 7.
Testcase 2: 4th smallest elemets in the given array is 15.
 
'''



#-------------------------custom code-------------------------------
t=int(input("Enter test Cases: "))
for i in range(t):
    A=[]
    n=int(input("Enter Size of THe Array: "))
    print("Enter The Array Element: ")
    for i in range(n):
        a=int(input())
        A.append(a)
    print(A)
    k=int(input("Enter Kth smallest element: "))
    A.sort()
    print(A)
    if k<=n:
        array_elemnt=A[k-1:k]
        print(array_elemnt)
    else:
        print("k is larger then array of size!!!!")


#-------------------------------GFG code----------------------------
# t=int(input())
# for i in range(t):
#     n=int(input())
#     A=list(map(int,input().split()))
#     k=int(input())
#     A.sort()
#     if k<=n:
#         array_elemnt=A[k-1:k]
#         for i in range(len(array_elemnt)):
#             print(array_elemnt[i])