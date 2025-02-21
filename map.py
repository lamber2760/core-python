def cube(x):
    return x * x * x
print(cube(2))    




l =[1,2,3,4,5,6]
newlist=[]
for item in l:
    newlist.append(cube(item)) 
print(newlist) 

emp =[8,7,6,5,4,3,2,1]
a = list(map(cube,emp))
print(a)