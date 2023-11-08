from random import *
x= randint(1,10)
c= 0
m=5
print(" Welcome to the number guessing game")
def guess_number(num):
    print("Please make a guess for the number")
    y=int(input())
    global c
    global m

    while c!=5:
        c+=1
        m-=1
        if y==num:
            print("Correct guess!")
            print(f"You got it correct in {c} tries")
            break
        elif y>num:
            print("Your guess is too high")
            print(f"You got only {m} tries")
            guess_number(x)
            break
        elif y<num:
            print("Your guess is too low")
            print(f"You got only {m} tries")
            guess_number(x)
            break
    else:
        print("You are out of guesses")
guess_number(x)