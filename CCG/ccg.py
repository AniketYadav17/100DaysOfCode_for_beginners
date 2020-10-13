#Colors Choices Game (CCG) coding in python
#(red, yellow, orange, green, blue)

import random


def goodbye(play):
    if play == 'n':
        print('Alright! See you soon.')
    else:
        print('Invalid Entry. Game Closed.')


#The start part of the code where we define the set of colors 
# users and computer will pick from.
colors = ('red', 'orange', 'yellow', 'green', 'blue')
play = 'y'
player_score = 0
comp_score = 0

# Loop to ask the player to play for as long as he wishes too.

while play == 'y':
    color = input("Enter color: ")
    comp_choice = random.choice(colors)                                 # Computer chooses it's color

    if color in colors:
        print("Good color choice.")
    else:
        print("Invalid Color choice. Game Closed.")
        break
    
    if comp_choice == color:
        print("The computer's choice is", comp_choice)
        print("You Won. Congratulations!")
        player_score += 1                                               # Count player score
    else:
        print("The computer's choice is", comp_choice)
        print("You lose :(")
        comp_score += 1                                                 # Count comp score
        
    print("Score \n Your =", player_score, "Computer =", comp_score,'\n')
    play  = input('Play again? (y/n): ')                                # If players wants to play again or not.
    
    if play == 'y':                                         
        pass
    else:
        goodbye(play)
