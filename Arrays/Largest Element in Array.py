# Largest Element in Array
# Given an array a[] of size N. The task is to find the largest element in it.

# Input:
# The first line of input contains an integer T, denoting the number of testcases. Then T test cases follow. Each test case contains an integer N , the number of elements in the array. Then next line contains N integers of the array separated by space.

# Output:
# Print the maximum element in the array. 
# Example:
# Input:
# 2
# 5
# 10 324 45 90 9808
# 7
# 1 2 0 3 2 4 5

# Output:
# 9808
# 5
import array as arr
#---------------------------------normal code------------------------------------
T=int(input("Enter test case: "))
for i in range(T):
    lsit1=[]
    N=int(input("Enter Size of Array: "))
    print("Enter Array elemnt: ")
    for i in range(N):
        ar=int(input())
        lsit1.append(ar)
    A=arr.array('i',lsit1)
    largest_element=max(A)
    print(largest_element)



#----------------------------GFG code(competitive coding)----------------------------
# T=int(input())
# for i in range(T):
#     N=int(input())
#     A=list(map(int,input().split()))
#     largest_element=max(A)
#     print(largest_element)