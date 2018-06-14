# Name:
# Date:


# proj05: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    infile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string

    line = infile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
word = choose_word(wordlist)


var = string.lowercase

X = []
for letter in word:
    X.append(letter)
d = []
for letter in word:
    d.append("_")

sum = 5



cows = len(word)
print ("The avaliable letters are ") + str(var) + (".")
chickens = raw_input(str("Welcome to hangman! You have up to seven guesses. I am thinking of a word with ") + str(cows) + str(" letters.") + str(" Guess a letter or type 'exit' to leave."))
var = var.replace(chickens, "")
print ("You have this many letters left.") + str(var)

while chickens != str("exit") and X != word and sum != 0:
    if chickens not in X:
        if int(sum) == int(5):
            print "o"
        if d != word:
            sum = sum - int(1)
        chickens = raw_input(("Incorrect! You can guess another letter or type 'exit' to leave the game.") + (" You have ") + str(sum) + (" guesses left."))
        var = var.replace(chickens, "")
        print "You have this many letters left." + str(var)
        if chickens not in X:
            if int(sum) == int(4):
                print "o-"
            if chickens not in X:
                if int(sum) == int(3):
                    print "o-|"
            if chickens not in X:
                if int(sum) == int(2):
                    print "o-|-"
            if chickens not in X:
                if int(sum) == int(1):
                    print "o-|-<"
            if sum == int(0):
                print "You lost! The word was " + word + "."


    else:
        counter = 0
        for letter in word:
            if letter == chickens:
                d[counter] = chickens
            counter = counter + 1
        print d
        chickens = raw_input("You guessed correctly! Guess another letter or type 'exit' to leave the game.")
        var = var.replace(chickens, "")
        print "You have this many letters left." + str(var)


















