"""A number-guessing game."""

# Put your code here
import random

print("Hello. Let's play a game. ")
user_name  = input("Enter your name: ")
rand_num = random.randint(0,101)

guess_count = 0


for i in range(rand_num):
    user_guess = int(input(f'{user_name}, guess a number between 1 and 100.'))
    if user_guess != rand_num:
        if user_guess > rand_num:
            print("Too high. Guess again.")
        elif user_guess < rand_num:
            print("Too low. Guess again.")
    guess_count = guess_count + 1
    if user_guess == rand_num:
        print(f'game over. Total guess: {guess_count}')
        break
    
#import random
#create random number val and generate
# assign input function asking for number in range
#for loop
#guess count function
#total count function
#game over output

