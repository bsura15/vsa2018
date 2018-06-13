# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""


import random
variable_number = random.randint(1, 9)
user_input = raw_input("Im thinking of a number between 1 and 9. There is a limitation of 5 guesses. Can you guess my number? Enter a number, or 'exit' to end the game:")


sum = 1



while user_input != str("exit") and sum < 5:
    if int(user_input) > variable_number:
        print "Your number is too high!"
        sum = sum + 1
        user_input = raw_input("Enter a number, or 'exit' to end the game.")
    elif int(user_input) < variable_number:
        print "Your number is too low!"
        sum = sum + 1
        user_input = raw_input("Try again.")
    elif int(user_input) == variable_number:
        print "Congratulations, you guessed my number!"
        print str("You used " + str(sum) + str(" guess(es)."))
        break




