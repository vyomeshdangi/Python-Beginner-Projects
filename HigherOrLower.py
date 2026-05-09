import random

print("""Welcome to the game of Higher or Lower
Instructions : 
you have to guess a number between 1 and 100
If you guess the number lower than the winning number program will say "higher!" 
If you guess the number higher than the winnning number program will say "lower!" 
there will be three levels.. as level increases range of numbers will too""")

yn = input("start game ? (y/n) ")

def game(range,attempts):
    winningnumber = random.randint(1,range)
    print(f"The range is 1-{range}")
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
    levelinput = input("which level (1,2,3 or IMPOSSIBLE) : ")

    if levelinput == "1":
        game(10,10)

    elif levelinput == "2":
        game(50,10)

    elif levelinput == "3":
        game(100,10)

    elif levelinput == "IMPOSSIBLE":
        game(1000000000000000000000000,1000000)

    else:
        print("try again !") 

else:
    print("why did you even run if you don't want to play ..?")   