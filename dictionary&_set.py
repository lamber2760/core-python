
## dict 

# info = {
#     "key" : "value",
#     "name" : "sachin",
#     "age" : 24,
#     "marks" : [45,65,76],
#     "tuple" : ("dict","key")
#     }

# print(info)
# print(type(info))


### nested dictinary##

# students = {
#     "name" : "lucky",
#     "marks" :{
#         "chem" : 78,
#         "math" : 89,
#         "hind" : 89,        
#     }
# }

# print(students)


########### dictionary method ##########
# students = {
#     "name" : "lucky",
#     "marks" :{
#         "chem" : 78,
#         "math" : 89,
#         "hind" : 89,        
#     }
# }
# print(students()) 

# list1 = [1,2,3,4,5,6,7,8,9,10]
# print(list1[::3])


# lst = [1,4,54,65,78,2]


# dictionary


# dictionary = {
#     "table" : ("a pices of furiturre","list is the number"),  ## use []
#     "cat" : "a small animal"
# }
# print(dictionary)
 
# subjects ={
#     "pyhton","java","c++","pyhton","javascript","java",
#     "pyhton","java","c++","c"

# }
# print(subjects)
# print(len(subjects))
# len(subjects)



 
# marks = {}
# x = int(input("enter your merks phy :"))
# marks.update({"phy" : x})
# y = int(input("enter your merks math :"))
# marks.update({"math" : y})
# z = int(input("enter your merks peng :"))
# marks.update({"peng" : z})
# print(marks)


# for i in range(10):
#     print(i * "*")
# for j in range(10,0,-1):
#     print(j * " *")  



d={}
name = input("enter your name : ")
lamp = input("enter your lamp : ")
d.update({name:lamp})
name = input("enter your name : ")
lamp = input("enter your lamp : ")
d.update({name:lamp})
name = input("enter your name : ")
lamp = input("enter your lamp : ")
d.update({name:lamp})
print(d)