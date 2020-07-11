# Palindromic Array
# Given a Integer array A[] of n elements. Your task is to complete the function PalinArray. Which will return 1 if all the elements of the Array are palindrome otherwise it will return 0.
# Example:
# Input:
# 2
# 5
# 111 222 333 444 555
# 3
# 121 131 20

# Output:
# 1
# 0

# Explanation:
# For First test case.
# n=5;
# A[0] = 111    //which is a palindrome number.
# A[1] = 222   //which is a palindrome number.
# A[2] = 333   //which is a palindrome number.
# A[3] = 444  //which is a palindrome number.
# A[4] = 555  //which is a palindrome number.
# As all numbers are palindrome so This will return 1.

#-----------------------custom code---------------
def palindrome(arr,n):

    for i in range(n):
        new_array=str(arr[i])
        rev=new_array[::-1]
        if new_array != rev:
            return 0
    return 1


T=int(input("Test Cases: "))
for i in range(T):
    arr=[]
    n=int(input("Enter The Size Array: "))
    print("enter The Element")
    for i in range(n):
        A=int(input())
        arr.append(A)
    print(arr)
    if palindrome(arr,n):
        print(1)
    else:
        print(0)
    # for i in range(N):
    #     new_array=str(list1[i])
    #     rev=new_array[::-1]
    #     if new_array == rev:
    #        return True
    # return False

    #--------------------------------GfG code ------------------

    
# def PalinArray(arr ,n):
    
#     # Code here
#     for i in range(n):
#         new_array=str(arr[i])
#         rev=new_array[::-1]
#         if new_array != rev:
#             return 0
#     return 1
# t=int(input())
# for i in range(t):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     if PalinArray(arr,n):
#         print(1)
#     else:
#         print(0)