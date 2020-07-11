import array as arr
T=int(input("Enter Test case: "))
while T>0:   # here we can use for i in range (0,T)
    list1=[]
    N=int(input("size of array: "))
    for i in range(N):
        ar=int(input())
       
        list1.append(ar)
    A=arr.array('i',list1)
    for i in range(0,N):
        print(A[i],end=" ")
    print()
    sum=0
    for i in range(N): # here we can use length of array  len(A)
        sum +=A[i]
    print(sum)
    #here we can use second way 
    #here sum() is inbuilt function in python
    # print(sum(A))
