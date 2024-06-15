from random import choice
import string

MAX_WRONG_GUESSES = 6

def select_word():
    with open('words.txt', 'r') as file:
        list_words = file.readlines()
    return choice(list_words).strip()

def get_letter_input(guessed_letters):
    while True:
        letter_input = input('Guess a letter: ').lower()
        if _valid_letter_input(letter_input, guessed_letters):
            return letter_input
        else:
            return 'Input a lower letter and not in the guessed list.'

def _valid_letter_input(letter_input, gussed_letter):
    return (
        len(letter_input) == 1
        and letter_input in string.ascii_lowercase
        and letter_input not in gussed_letter
    )

def build_guessed_word(answer_word, guessed_letters):
    list_guessed_letters = []
    for letter in answer_word:
        if letter in guessed_letters:
            list_guessed_letters.append(letter)
        else:
            list_guessed_letters.append('_')
    return ' '.join(list_guessed_letters)

# hangman.py
# ...

def draw_hanged_man(wrong_guesses):
    hanged_man = [
        r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
    ]

    print(hanged_man[wrong_guesses])

def game_over(wrong_guesses, answer_word, gussed_letters):
    return (
        wrong_guesses == MAX_WRONG_GUESSES
        or set(answer_word) <= gussed_letters
    )

if __name__ == '__main__':
    answer_word = select_word()
    print(answer_word)
    guessed_letters = set()
    gussed_word = build_guessed_word(answer_word, guessed_letters)
    wrong_guesses = 0
    print('----------------------Welcome to Hangman!----------------------\n')

    while not game_over(wrong_guesses, answer_word, guessed_letters):
        #draw_hanged_man(wrong_guesses)
        print(f'Your word need to guess is: {gussed_word}\n')
        print(f'Words you have gussed: {' '.join(sorted(guessed_letters))} \n')

        player_input = get_letter_input(guessed_letters)
        if player_input in answer_word:
            print('It is a great guess!')
            print('--------------------------------------------')
        else:
            wrong_guesses += 1
            print('It is not there. Try again!')
            print('--------------------------------------------')
        
        guessed_letters.add(player_input)
        gussed_word = build_guessed_word(answer_word, guessed_letters)
    
    #draw_hanged_man(wrong_guesses)
    if wrong_guesses == MAX_WRONG_GUESSES:
        print('Sorry, you lost!')
    else:
        print('Congrats! You did it!')
    print(f'Your word is: {answer_word}')
