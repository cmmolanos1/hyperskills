""" Hangman Game """

import random
import string

# List of words to guess
word_list = ['python', 'java', 'kotlin', 'javascript']

# Choose the word randomly
word = random.choice(word_list)

# Create a set with the right letters
letters = set(word)

# Create a list of typed letters
typed_letters = []

# Create the guessed word to be printed
guessed_list = list('-' * len(word))

# Prompt
print('H A N G M A N')
while True:
    action = input('Type "play" to play the game, "exit" to quit: ')
    if action == 'play':

        lives = 8

        while True:
            if lives > 0:
                print()
                # Join the list to make a string
                print("".join(guessed_list))
                if '-' not in guessed_list:
                    print("You guessed the word!\nYou survived!")
                    break

                target = input("Input a letter: ")

                if len(target) != 1:
                    print("You should print a single letter")

                else:
                    if target not in string.ascii_lowercase:
                        print("It is not an ASCII lowercase letter")

                    else:
                        if target in letters and target not in typed_letters:
                            for i in range(len(word)):
                                if word[i] == target:
                                    guessed_list[i] = target

                        elif target in typed_letters:
                            print("You already typed this letter")

                        else:
                            print("No such letter in the word")
                            lives -= 1
                typed_letters.append(target)
            else:
                print("You are hanged!")
                break

    if action == 'exit':
        break
