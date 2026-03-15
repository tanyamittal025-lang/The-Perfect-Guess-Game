#The Perfect Guess Game 
import random

print("welcome to the intuition game")

n=random.randint(1,100)
a=-1
guess=0

while(a!=n):

    a=int(input("guess the number between 1 and 100: "))
    if a<n:
        print("higher number please")
        guess+=1

    elif a>n:
        print("lower number please")
        guess+=1

print(f"Congrats! You guessed the correct number {n} after {guess} guesses.")

