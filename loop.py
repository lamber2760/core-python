##### print numbers from 1 to 100 .....?
# 
#  i = 1
# while i<=100:
#     i += 1
#     print(i)

######### print number from 100 to 1 ???


# i = 100
# while i>=1:
#     print(i)
#     i -= 1
    


### print the multiplecation table of a number n   .?????


# tab = int(input("enter your table name : " ))
# i = 1
# while i <= 10:
#     print(tab,"x",i,"=",i*tab)
#     i += 1



#qusr 4

## print the element of the  following list using a loop 
# nums = [1,4,9,16,25,36,49,64,82,100]
# # print(len(nums))
# idx = 0

# while idx < len(nums):
#     print(nums[idx])
#     idx += 1

#ques  5

# tup = (1,4,9,16,25,36,49,64,82,100)
# i =  0
# while i < len(tup):
#     print(tup[i])
#     i +=1

# tup = (1,4,9,16,25,36,49,64,82,100)
# i =  0
# x=36
# while i < len(tup):
#     if (tup[i]==x):
#         print("found in ind",i)
#     i +=1 

# for i in range(5):
#     print( "*"*i)
#     for j in range(5,5):
#         print("*"*i)
          

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")   
#     print("\n")                                      # for i in range(1,6):
                                                     # #     print( "*" * i )


# for i in range(6,0,-1):
#     print("*" * i)

# for i in range(6,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")   
#     print("\n") 

# for i in range(1,6):
#     for k in range(1,6-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end="")   
#     print("\n")

# for i in range(6,0,-1):
#     for k in range(1,6-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end="")   
#     print("\n")

# for i in range(6,0,-1):
#     for k in range(1,6-i):
#         print(" ",end="")
#     for j in range(1,(2 * i-1)+1):
#         print("*",end="")   
#     print("\n")

 ########### question 1



a = input("enter your number : ")

num = int(input("enter your number :"))

if num % 5 == 0:
    print("hello ",a)
else:
    print("Bye ",a)    

   
######## question 2
for i in range(1,100):
    if i % 5 == 0 and i % 7 == 0:
        print(i)


### question  3

a =[1,2,3,4,5,6,7,8,9,10]
even_num= 0
odd_num =0

for i in a:
    if i % 2 == 0:
        even_num +=1
    else:
        odd_num +=1
print("this is even number",even_num)
print("this is odd number",odd_num)   


### question  4


for i in range (1,11):
    if  (i % 3 == 0 or i % 6 == 0):
        continue
    print(i)    


 






