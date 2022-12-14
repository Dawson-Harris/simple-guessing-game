#Guessing Game by Dawson Harris
#A random number is selected and the user must guess
#import module and variable names

import random
guess_counter = 1
guess = None
too_high = "Too high, try again"
too_low = "Too low, try again."
secret = random.randint(1, 100)
congrats = "Congratulations, You Won! It took you "

#This loop takes the user input and converts from string to integer

while guess != secret:
    guess = int(input("What is the magic number? "))
    
    #This section checks the users input against the random number
    #And increments the guess counter after every wrong answer
    
    if guess < secret:
        print(too_low)
        guess_counter+=1
    elif guess > secret:
        print(too_high)
        guess_counter+=1
   
    #This section determines the 'Game Over' message based on tries 
   
    elif guess == secret and guess_counter == 1:
        print(congrats + str(guess_counter) + " guess.")
    else:
        print(congrats + str(guess_counter) + " guesses.")
