import random

print("""Welcome to the game of Higher or Lower
Instructions : 
you have to guess a number between 1 and 100
If you guess the number lower than the winning number program will say "higher!" 
If you guess the number higher than the winnning number program will say "lower!" 
there will be three levels.. as level increases range of numbers will too""")

yn = input("start game ? (y/n) ")

def game_level_1():
    attempts = 10
    winningnumber = random.randint(1, 10)
    print("The range is 1-10")
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
        
def game_level_2():
    attempts = 10
    winningnumber = random.randint(1, 50)
    print("The range is 1-50")
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

def game_level_3():
    attempts = 10
    winningnumber = random.randint(1, 100)
    print("The range is 1-100")
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
    levelinput = input("which level (1,2 or 3) : ")

    if levelinput == "1":
        game_level_1()

    elif levelinput == "2":
        game_level_2()

    elif levelinput == "3":
        game_level_3()

    else:
        print("try again !")    