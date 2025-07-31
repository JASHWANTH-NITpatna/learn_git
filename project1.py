name = input("Enter Your Name: ")
print("Hello "+name+" welcome to my game!")

play=input(name+" Do you wanna play (Yes/No) ?)").lower()

if play == "yes":
    print(name+" We are gonna play ...")
    direction=input(name+" Enter The direction you wanna go (left/right)").lower()
    if direction=="left":
        print(name+" You went left and fell of a cliff, game over, try again.")
    elif direction=="right":
        choice=input("Okay, you now see a bridge, do you want to swim under it or cross it? (swim/cross)").lower()
        if choice=="swim":
            print("You got eaten by alligator, you die,the end!")
        else:
            print("You found the gold and won!")    
    else:
        print(name+" Sorry not valid replay, You die !")



else:
    print(name+" We ar  e not gonna play ...")
print("!END!")
print("END")
