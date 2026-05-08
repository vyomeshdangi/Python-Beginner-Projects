import random

print("""Welcome to the game of Higher or Lower
Instructions : 
you have to guess a number between 1 and 100
If you guess the number lower than the winning number program will say "higher!" 
If you guess the number higher than the winnning number program will say "lower!" 
you will have seven attempts !""")

yn = input("start game ? (y/n) ")

def game():
    attempts = 7
    winningnumber = random.randint(1, 100)
    print("guessing number......")
    print("done !")
    # print(winningnumber)   
    guess = None
    
    while guess != winningnumber and attempts != 0:
        guess = int(input(f"Enter your guess ({attempts} tries left): "))
        attempts -= 1 

        if guess > winningnumber:
            print("lower !")
            
        elif guess < winningnumber:
            print("higher!")

        else :
            print("CORRECT !")

    if guess == winningnumber:
        print(f"you won! with {attempts} number of attempts left")

    else:
        print("all attempts used! game over !")
        print(f"the answer was {winningnumber}")
    
    
if yn == "y":
    game()