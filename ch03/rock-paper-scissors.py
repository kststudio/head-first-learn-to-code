# Here we're doing some setup by importing the random module and setting up the winner variable
import random

winner = ''

# The computer randomly chooses rock, paper, scissors by generating a random number from 0 to 2 and then mapping that to a corresponding string
random_choice = random.randint(0, 2)

if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

# The game logic: checks to see if the computer wins or note, and makes theappropriate change to the winner variable
user_choice = ''

while(user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissors'):
    user_choice = input('rock, paper, or scissors?')
    

if computer_choice == user_choice:
    winner = 'Tie'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'
else:
    winner = 'User'

# Announce if the game is either a tie or the winner of that round. Share the computer's choice.
if winner == 'Tie':
    print('We both choose', computer_choice + '. Try again!')
else:
    print(winner, 'won. The computer chose', computer_choice + '.')

