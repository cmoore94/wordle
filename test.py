from os import linesep
import random

class color:
   GREEN = '\033[1;32;48m'
   YELLOW = '\033[1;33;48m'
   RED = '\033[1;31;48m'
   END = '\033[1;37;0m'

f = open("wordlist")

words = []
lines = f.readlines()

for line in lines:
    if len(line) >= 2:
        words.append(line.strip().lower())

random_word = random.choice(words)
#print(random_word)

guesses = 1
won = False

while guesses <= 6 and won == False:
    ask_string = "Guess " + str(guesses) + ": "
    val = raw_input(ask_string)
    print(val)
    if len(val) == 5 and val in words:
        coloured_out = ""
        for i, letter in enumerate(val):
            if letter == random_word[i]:
                coloured_out += color.GREEN + letter
            elif letter in random_word:
                coloured_out += color.YELLOW + letter
            elif letter not in random_word:
                coloured_out += color.RED + letter
        coloured_out += color.END
        print(coloured_out)
        guesses += 1
    else:
        if len(val) < 5:
            print("word must be 5 letters long")
        if val not in words:
            print("word not in dictionary")
    if val == random_word:
        won = True
        print("You win!")