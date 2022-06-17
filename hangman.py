#########################################################################################################
# https://github.com/visheshdvivedi/Top-10-Easy-Python-Project-Ideas-For-Beginners/blob/main/hangman.py #
#########################################################################################################
import random
import os

def get_random_word_from_wordlist():
    path = os.getcwd()
    filename = 'hangman_wordlist.txt'
    file_with_words = path + os.path.sep + filename
    with open(file_with_words, 'r') as f:
        wordlist = f.read().split()
    word = random.choice(wordlist)
    return word

def get_some_letters(word):
    letters = list(word)
    temp = '_' * len(word)
    character = random.choice(letters)
    for num, char in enumerate(letters):
        if char == character:
            templist = list(temp)
            templist[num] = char
            temp = ''.join(templist)
    return temp

def draw_hangman(chances):
    if chances == 0:
        print("---------")
        print("   ( )-| ")
        print("  - | -  ")
        print("   / \   ")
    elif chances == 1:
        print("---------")
        print("   ( )-  ")
        print("  - | -  ")
        print("   / \   ")
    elif chances == 2:
        print("---------")
        print("   ( )   ")
        print("  - | -  ")
        print("   / \   ")
    elif chances == 3:
        print("---------")
        print("   ( )   ")
        print("  - | -  ")
        print("   /     ")
    elif chances == 4:
        print("---------")
        print("   ( )   ")
        print("  - | -  ")
        print("         ")
    elif chances == 5:
        print("---------")
        print("   ( )   ")
        print("    |    ")
        print("         ")
    elif chances == 6:
        print("---------")
        print("   ( )   ")
        print("         ")
        print("         ")

def start_hangman_game():
    word = get_random_word_from_wordlist()
    temp = get_some_letters(word)
    chances = 7
    found = False
    while True:
        if chances == 0:
            print(f"Sorry, you lost... The word was: {word}")
            break
        print("=== Guess the word ===")
        print(temp, end='')
        print(f"\t(Word has {len(word)} letters)")
        print(f"Chances left: {chances}")
        character = input("Enter the character you think the word may have: ")
        if len(character) > 1 or not character.isalpha():
            print("Please enter a single alphabet only")
            continue
        else:
            for num, char in enumerate(list(word)):
                if char == character:
                    templist = list(temp)
                    templist[num] = char
                    temp = ''.join(templist)
                    found = True
        if found:
            found = False
        else:
            chances -= 1
        if '_' not in temp:
            print(f"\nYou Won!!! Then word was: {word}")
            print(f"You got it in {7 - chances} chances")
            break
        else:
            draw_hangman(chances)
            print()

print(f"===== Welcome To Hangman Game =====")
while True:
    choice = input("Do you want to play hangman (y/n): ")
    if choice.lower() == 'y':
        start_hangman_game()
    elif choice.lower() == 'n':
        print(f"Exiting....")
        break
    else:
        print(f"Invalid input... Please try again")
print("\n")





