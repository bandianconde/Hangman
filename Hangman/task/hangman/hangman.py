# Write your code here
from random import choice
from string import ascii_lowercase


def get_masked_word(word, provided_letters):
    letters = list(word)
    masked_word = ['-' if letter not in provided_letters else letter for letter in letters]
    return ''.join(masked_word)


def word_is_discovered(provided_correct_letters, choosen_word_letters):
    return provided_correct_letters == choosen_word_letters


def user_input_is_valid(letter: str):
    if len(letter) != 1:
        print("Please, input a single letter.")
        return False
    else:
        if letter not in ascii_lowercase:
            print("Please, enter a lowercase letter from the English alphabet.")
            return False
    return True


def play():
    choosen_word = choice(valid_words)
    choosen_word_letters = set(choosen_word)
    provided_correct_letters = set()
    provided_letters = set()
    remaining_attempts = 8
    while remaining_attempts > 0 and not word_is_discovered(provided_correct_letters, choosen_word_letters):
        print(get_masked_word(choosen_word, provided_correct_letters))
        letter = input("Input a letter: ")
        if user_input_is_valid(letter):
            if letter in provided_letters:
                print("You've already guessed this letter.")
            elif letter in choosen_word_letters:
                if letter not in provided_correct_letters:
                    provided_correct_letters.add(letter)
            else:
                print("That letter doesn't appear in the word.")
                remaining_attempts -= 1
            provided_letters.add(letter)

    print()
    if word_is_discovered(provided_correct_letters, choosen_word_letters):
        print(f"You guessed the word {choosen_word}!")
        print("You survived!")
        results['wins'] += 1
    else:
        print("You lost!")
        results['losses'] += 1


def show_results():
    print(f'You won: {results["wins"]} times.')
    print(f'You lost: {results["losses"]} times.')


valid_words = ["python", "java", "swift", "javascript"]
results = {'wins': 0, 'losses': 0}
print("H A N G M A N")
while True:
    while True:
        menu_choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        if menu_choice in ("play", "results", "exit"):
            break
    if menu_choice == "play":
        play()
    elif menu_choice == "results":
        show_results()
    else:
        break
