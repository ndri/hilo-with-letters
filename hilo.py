#!/usr/bin/env python
# Higher or Lower with base26
import random

alphabet = u"abcdefghijklmnopqrstuvwxyz"
tries = 0

# Function to convert a base26 word into a decimal number
def numerize(word):
    # Add up all combinations for lengths lower than the current length
    count = sum([len(alphabet)**i for i in range(len(word))])
    # Create a variable for the possible combinations of the current length
    combinations = len(alphabet)**(len(word))
    # Do the rest
    for letter in word:
        combinations /= len(alphabet)
        count += alphabet.index(letter) * combinations
    return count

# Choose secret word
secret = ''.join([random.choice(alphabet) for i in range(random.randint(1,7))])
secretnumber = numerize(secret)

# Start the game
while 1:
    try:
        guess = raw_input("Guess a word: ")
        # Check wether all letters in the guess are in the alphabet
        if any(letter not in alphabet for letter in guess):
            raise ValueError
        elif numerize(guess) < secretnumber:
            print "Higher."
        elif numerize(guess) > secretnumber:
            print "Lower."
        else:
            print "Congratulations, you won with {0} tries!".format(tries)
            break
        tries += 1
    except ValueError:
        print "Try again."
    except KeyboardInterrupt:
        print "\nGood bye."
        break
