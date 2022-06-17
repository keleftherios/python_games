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


def get_letter_from_word(word):
    letters = list(word)
    temp = '_ ' * len(word)
    character = random.choice(letters)
    for index, char in enumerate(letters):
        if char == character:
            templist = temp.split()
            templist[index] = char
            temp = ' '.join(templist)
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


def hangman_game():
    word = get_random_word_from_wordlist()
    word_to_display = get_letter_from_word(word)
    wrong_letters = list()
    chance = 7
    letter_found = False
    while True:
        if chance == 0:
            print(f"Sorry you lost... The word was: {word}")
            break
        print(f"=== Guess the word ===")
        print(word_to_display)
        print(f"Letters to find: {word_to_display.count('_')}")
        print(f"        Chances: {chance}")
        print(f"  Wrong letters: {wrong_letters}")
        character = input("Enter a character: ")
        if len(character) > 1 or not character.isalpha():
            print(f"Please enter a single alphabet character.")
            continue
        else:
            for num, char in enumerate(list(word)):
                if character == char:
                    temp_display = word_to_display.split()
                    temp_display[num] = character
                    word_to_display = ' '.join(temp_display)
                    letter_found = True
        if letter_found:
            letter_found = False
        else:
            wrong_letters.append(character)
            chance -= 1
        if '_' in word_to_display:
            draw_hangman(chance)
            print()
        else:
            sentence = "Congratulations!!! You found the word: " + word
            print("\n=" * len(sentence))
            print(sentence)
            print("=" * len(sentence))
            print()
            break






def main():
    while True:
        print(f"===== Welcome To Hangman Game =====")
        user_input = input("Do you want to play Hangman game (y/n): ")
        if user_input.lower() == 'y':
            hangman_game()
        elif user_input.lower() == 'n':
            print(f"Exiting...")
            break
        else:
            print(f"Invalid input... Please try again")
    print()

if __name__ == "__main__":
    main()
