# a = int(input("enter your age : "))

# if (a>18):
#     print("your are above  the age of consent ")
# else:
#     print("your are below the age of consent")  


# print("end of program")    






# num = int(input("enter your value  : "))

# # a = num % 2
# if (num % 2 == 0):
#     print("even")
# else:
#     print("odd")


# num1 = int(input("enter your number 1 :")) 
# num2 = int(input("enter your number 2:")) 
# num3 = int(input("enter your number 3:")) 
# num4 = int(input("enter your number 4:")) 

# if (num1>num2 and num1>num3 and num1>num4):
#     print("this is grestest num1 ",num1)
# elif (num2>num1 and num2>num3 and num2>num4):
#     print("this is grestest num2 ",num2)
# elif (num3>num1 and num3>num2 and num3>num4):
#     print("this is grestest num3 ",num3)
# elif (num4>num1 and num4>num2 and num4>num3):
#     print("this is grestest num4 ",num4)    
    

# student1= int(input("enter your marks  student 1: "))
# student2= int(input("enter your marks  student 2: "))
# student3= int(input("enter your marks  student 3: "))

# total_percentage = 100 *(student1 + student2 + student3)/300

# if (total_percentage >=40 and student1>=33 and student2 >=33 and student3 >= 33):
#     print("you are pass" ,total_percentage)

# else:
#     print("your are fail",total_percentage)    
  


# p1 = "this is one"
# p2 = "this is teo"
# p3 = "this is three"
# p4= "this is forth"

# mess = input("enter your comment")
# if ((p1 in mess)  or (p2 in mess) or (p3 in mess) or (p4 in mess)):
#     print("this is comment is span")

# else:
#     print("this is comment is ini=ot sdadfvsvs ")    


# name = input("enter  your name  :")
# if (len(name )<10):
#     print("your name contain less than 10 characters")
# else:
#     print("all is well")    



    




# l = ["lucky" ,"sachn" ,"shanuxj","sdjfkjs","sdjf"]
# name = input("enter your name :")
# if(name in l):
#     print("your name in the list")

# else:
#     print("your name is not a list")    






marks = int(input("enter your marks : "))
if (marks <=100 and marks >=90):
    garde = "EX"
elif (marks <90 and marks >=80):
    garde = "A"
elif (marks <80 and marks >=70):
    garde = "B"
elif (marks <70 and marks >=60):
    garde = "C"
elif (marks <60 and marks >=50):
    garde = "D"
elif (marks <=100 ):
    garde = "F"

print("your garde is ",garde)    