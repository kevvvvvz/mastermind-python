import random
import sys

def two_player_mode():
    ...


def compTurn():
    number = random.randrange(1000, 10000)
    number = str(number)
    print()
    attempts = 0
    
    print("X X X X")
    while True:
        guess = input("Enter a number guess containing 4 digits: ")
        if len(guess) != 4 or not guess.isdigit():
            print()
            print("Please ensure guess contains 4 digits")
            continue
        
        for i, char in enumerate(number):
            if guess[i] == char:
                print(char, end=" ")
            else:
                print("X", end=" ")
            
        if guess == number and attempts == 0:
            print()
            return "Guessed Immediately: You WIN!"
            
        if guess == number:
            print()
            return "Number correctly guessed, You Win!"
        
        if guess != number:
            print()
            print("Incorrect, continue guessing!")
            attempts += 1
            print()
            print("Attempt Counter:", attempts)
        
            
def main():
    
    while True:
        print("Player 2 is Computer.")
        result = compTurn()
        print(result)
        check = input("Would you like to play again? Enter (Yes/No): ").upper()
        if check == "NO":
            sys.exit()
    

main()