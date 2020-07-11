# Print alternate elements of an array

# You are given an array A of size N. You need to print elements of A in alternate order

# Input Format:
# The first line of input contains T denoting the number of testcases. T testcases follow. Each test case contains two lines of input. The first line contains N and the second line contains the elements of the array

# Output Format:
# For each testcase, print the alternate elements of the array(starting from index 0)

# Your Task:
# Since this is a function problem, you just need to complete the provided function void print(int ar[],int n)


# Example:
# Input:
# 2
# 4
# 1 2 3 4
# 5
# 1 2 3 4 5
# Output:
# 1 3
# 1 3 5

# Explanation:
# Testcase1: print 1, then 3
# Testcase2: print 1, then 3, then 5

#-----------------------custom code-----------------------
def Alternate_array(arr,n):
    for i in range(0,n,2):
        print(arr[i],end=" ")

T=int(input("Enter test case: "))
for i in range(T):
    list1=[]
    N=int(input("Enter The Size of array: "))
    print("Enter Array Element: ")
    for i in range(N):
        arr=int(input())
        list1.append(arr)
    Alternate_array(list1,N)


#-------------------------GFG code(competive coding)--------------
# def printAl(arr,n):
#     # your code here
#     # for i in range(n):
#     #     re=random.randint(0,arr[i])
#     # print(re)
#     for i in range(0,n,2):
#         print(arr[i],end=" ")



# #{ 
# #  Driver Code Starts
# #Initial Template for Python 3

# if __name__=="__main__":
#     t=int(input())
#     for i in range(t):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         printAl(arr,n)
#         print()
# # } Driver Code Ends