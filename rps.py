import random
computer=random.choice(["rock","paper","scissors"])
user=input("enter your choice")
print("computer chose",computer,"you chose",user)
if user==computer:
    print("its a tie")
elif (user=="rock" and computer=="paper") or(user=="paper" and computer=="scissors" )or(user=="scissors" and computer=="rock"):
    print("you lost")
elif (computer=="rock" and user=="paper") or(computer=="paper" and user=="scissors" )or(computer=="scissors" and user=="rock"):
    print("you win!!!")      
else:
    print("not valid")    