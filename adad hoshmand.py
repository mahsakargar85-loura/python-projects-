import random 

number= random.randint(1,50)
tries=0

while True:
    guess= int(input("guess one num from 1 to 50:"))
    tries+=1

    if guess <number:
        print("go higher")
    elif guess > number:
        print("go lower")
    else:
        print (f"ecxellent you guess right!")  

        break