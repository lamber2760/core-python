# def fact(n):
#     if( n == 1 or n == 0):
#         return 1
#     return  fact(n - 1) * n  

# print(fact(6))    

## quwstion s1 21 

# def cal(n):
#     if ( n == 0):
#         return 0
#     return cal(n - 1) + n
# sum = cal(5)
# print(sum)

## queustion 232

# def print_list(list,indx = 0):
#     if (indx == len(list)):
#         return
    
#     print(list[indx])
#     print_list(list,indx + 1)

# fruits = [ "mango","apple","orange","banana"]     
# print_list(fruits) 


friend=["apple","orange",5,345,False,"honey","rohan"]
print(friend[-4])
friend[0]="mango"
print(friend[0])
print(friend)  