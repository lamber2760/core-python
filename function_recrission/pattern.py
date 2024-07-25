def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(5)    
     

for i in range(5,0,-1):
    print("*" * i)      