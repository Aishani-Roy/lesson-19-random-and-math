import random
number=random.randint(1,100)
while True:
    computer=int(input("enter your guess:"))
    if computer<number:
        print("this is too low")
    elif computer>number:
        print("this is too high")
    else:
        print("congrats!!")
        break 
    