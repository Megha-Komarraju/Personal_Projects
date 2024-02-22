import random

def guess_number():
    n = random.randint(1, 10)  # Using randint to include both 1 and 10
    while True:
        guess = int(input("Enter any number between 1 and 10: "))
        if guess < n:
            print("Too low")
        elif guess > n:
            print("Too high!")
        else:
            print("You guessed it right!!")
            res=input("Do you want to play again Y/N?")
            if res=='Y':
                continue
            else:
                break

guess_number()
