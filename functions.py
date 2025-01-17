import random


# RED   = "\033[1;31m"
# CYAN  = "\033[1;36m"
# GREEN = "\033[0;32m"
# RESET = "\033[0;0m"


def game_setup():
    words = game_read_file()
    rword = choose_random_word(words)
    hints = select_all_hints(words, rword)
    rword = rword[2:].strip().upper()
    return rword, hints


def game_read_file():
    file = open('game.txt', 'r', encoding='utf-8')
    words = file.readlines()
    file.close()
    return words


def choose_random_word(words):
    word = random.choice(words)
    while 'D:' in word:
        word = random.choice(words)
    return word


def select_all_hints(words, word):
    hints = []
    for i in range(len(words)):
        if (words[i] == word):
            k = i + 1
            while 'D:' in words[k]:
                hints.append(words[k][2:].strip())
                k += 1
                if (k == len(words)):
                    break
    return hints


def check_entry_validity(char):
    char = char.upper()
    if ((char.isalpha() and len(char) == 1) or char == 'HINT' or char == '9'):
        return True
    return False


def check_game_over(guesses, word):
    setword = set(word)
    guesses = set(guesses)
    if len(setword.difference(guesses)) == 0:
        return True
    return False


def choose_random_hint(hints):
    rhint = random.choice(hints)
    return 'Hint: ' + rhint


def check_used_arr(char, used_letters_array):
    if char in used_letters_array:
        return True


def check_correct_arr(char, word):
    if char in word:
        return True
    return False
