#!/usr/bin/env python
# Higher or Lower with Letters
import random

alphabet = u"abcdefghijklmnopqrstuvwxyz"
tries = 0
wordlist = "/usr/share/dict/words"

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

# Try to get word from the wordlist, otherwise choose a random combination
try:
    with open(wordlist) as f:
        words = f.read().decode('utf-8').splitlines()
    # Make sure every word is a legal word according to the alphabet
    words = filter(lambda word: not any(letter not in alphabet for letter in word), words)
    # Make sure there are some words left after the filter
    if len(words) == 0:
        raise
    secret = random.choice(words)
    print "Fetched the word from the wordlist!"
except:
    # If the wordlist doesn't exist, it chooses a random combination
    print "Failed to get a word from the wordlist, choosing random combination instead."
    secret = ''.join([random.choice(alphabet) for i in range(random.randint(2,7))])

secretnumber = numerize(secret)

# Start the game
print "Good luck!"

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
