# Maximum and Minimum Of Array Elements
'''
Example:
Input:
2
4
5 4 2 1
1
8

Output:
5 1
8 8

'''
#-------------------------custom code-----------------------------

t=int(input("enter test cases: "))
for i in range(t):
    list1=[]
    n=int(input("Enter size of array: "))
    print("Enter array elment: ")
    for i in range(n):
        a=int(input())
        list1.append(a)
    print(list1)
    maximum_elemnt=max(list1)
    minimum_element=min(list1)
    print(maximum_elemnt)
    print(minimum_element)

 #-----------------------------GFG code ----------------------------
#code
# t=int(input())
# for i in range(t):
#     n=int(input())
#     A=list(map(int,input().split()))
#     maximum_element=max(A)
#     minimum_element=min(A)
#     print(maximum_element,end=" ")
#     print(minimum_element)
    