import time
from functions import game_setup, choose_random_hint, check_game_over
from functions import check_entry_validity, check_used_arr, check_correct_arr


used_char_arr = []
wrong_guesses = []
right_guesses = []


def draw_game_screen(hint):
    global word
    print('\033[H\033[J', end='')
    print('\nType \'9\' to exit game\n')
    print('Wrong Guesses: ', ', '.join(wrong_guesses))
    print('\n')
    for char in word:
        if char in right_guesses or not char.isalpha():
            print(char, end='')
        else:
            print('_ ', end='')
    print('\n')
    if hint:
        print(hint)


def draw_end_screen():
    print('You Win!')
    time.sleep(1)


def reset_game():
    used_char_arr.clear()
    wrong_guesses.clear()
    right_guesses.clear()


def game_loop():
    global word, hints
    while True:
        char = input('\nType a letter or ask for a hint: ')
        valid = check_entry_validity(char)

        while not valid:
            char = input('\nInvalid. Type a letter or ask for a hint: ')
            valid = check_entry_validity(char)

        if char == '9':
            break
        else:
            char = char.upper()
            game_turn(char)


def game_turn(char):
    global word, hints
    if char == 'HINT':
        hint = choose_random_hint(hints)
        draw_game_screen(hint)
    else:
        if check_used_arr(char, used_char_arr):
            hint = f'You\'ve already guessed the letter {char}.'
            draw_game_screen(hint)
        else:
            used_char_arr.append(char)
            if check_correct_arr(char, word):
                right_guesses.append(char)
                draw_game_screen(None)
            else:
                wrong_guesses.append(char)
                draw_game_screen(None)
    game_turn_over()


def game_turn_over():
    global word, hints
    if check_game_over(right_guesses, word):
        draw_end_screen()
        reset_game()
        word, hints = game_setup()
        draw_game_screen(None)


def main():
    global word, hints
    word, hints = game_setup()
    draw_game_screen(None)
    game_loop()


main()
