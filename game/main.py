import random
'''
1  for snake 
-1 for water
0 for gun

'''
computer = random.choice([-1,0,1])
yourstr = input("Enter your choice :" )
yourdict = {"s" :1,"w" :-1,"g":0}
reversdict = {1:"snake",-1:"water",0:"gun"}


you = yourdict[yourstr]
print(f"your choice : {reversdict[you]}\ncomputer choice :{reversdict[computer]}")

if (computer== you):
    print("Its a draw")
else:
    if(computer == -1 and you == 1):
        print("you win !!") 

    elif(computer == -1 and you == 0):
        print("you LOse !!") 

    elif(computer == 1 and you ==-1):
        print("you Lose !!")

    elif(computer == 1 and you == 0):
        print("you win !!") 

    elif(computer == 0 and you == -1):
        print("you win !!") 

    if(computer == 0 and you == 1):
        print("you lose !!") 

    else:
        print("something went worng  ")    

