# Sum of Series
# Example:
# Input:
# 2
# 1
# 5

# Output:
# 1
# 15

#----------------------custom code-------------------
T=int(input("Enter test case: "))
for i in range(T):
    sum=0
    N=int(input("Enter size array: "))
    for i in range(N):
        sum +=i+1
    print(sum)


#---------------------GfG code----------------------
# T=int(input())
# for i in range(T):
#     sum=0
#     N=int(input())
#     for i in range(N):
#         sum +=i+1
#     print(sum)