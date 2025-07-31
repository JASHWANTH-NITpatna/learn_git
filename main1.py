import random

print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")

low =int(input("Enter the lowest Bound : "))
high=int(input("Enter the Highest Bound : "))

print("REMEMBER You have Only 7 chances to guess if You can't guess you are Out  !")

tar_num=random.randint(low,high)
tc=7
ch=0

while ch<tc:
    ch=ch+1
    num=int(input(f"Enter the number Your {ch}st choise :   ")) 
    if num==tar_num:
        print(f"Correct! You got the number {tar_num} , and you guessed in {ch} this many attempts !")
        break
    elif ch>=tc and num!=tar_num:
        print(f'Sorry! The number was {num}. Better luck next time.')
    elif num>tar_num:
        print(f" CLUES :- You guessed number is  Higher , Try Lower Number ")
    elif num<tar_num:
        print(f" CLUES :- You guessed number is  Lower , Try Higher Number ")
