T=int(input("Enter Test: "))
for i in range(T):
    N=int(input("Enter Array size: "))
    list1=[]
    print("Enter array elemnt: ")
    for i in range(N):
        A=int(input())
        list1.append(A)
    max_element=max(list1)
    list1.remove(max_element)
    second_max=max(list1)
    print("second largest number: ",second_max)







#-----------------------GFG--------------------------
# T=int(input())
# for i in range(0,T):
#     N=int(input())
#     A=list(map(int,input().split()))
#     m1=max(A)
#     A.remove(m1)
#     m2=max(A)
#     print(m2)