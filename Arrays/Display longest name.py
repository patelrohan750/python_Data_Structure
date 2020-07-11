print("hello")
T=int(input())
for i in range(0,T):
    list1=[]
    N=int(input())
    for j in range(N):
        nm=input()
        list1.append(nm)
    longest_string=max(list1,key=len)
    print(longest_string)
    
   
       
    




# a_list = ["a_string", "the_longest_string", "string"]
# longest_string = max(a_list, key=len)
# print(longest_string)