import time
import os
from functions import setUpGame, chooseRandomHint, checkIfCharIsCorrect
from functions import checkIfCharIsValid, checkIfCharWasUsed, checkIfGameIsOver


usedLettersArr = []
guessedLetters = []
incorrectGuess = []
correctGuesses = []


def drawGameScreen(word, hint):
    # print('\033[H\033[J', end='')
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\nDigite \'ESC\' para sair\n')
    print('Wrong Guesses: ', ', '.join(incorrectGuess))
    print('\n')
    for char in word:
        if char in correctGuesses or not char.isalpha():
            print(char, end='')
        else:
            print('_ ', end='')
    print('\n')
    if hint:
        print(hint)


def drawEndScreen():
    print('You Win!')
    time.sleep(1)


def clearAllArrays():
    usedLettersArr.clear()
    guessedLetters.clear()
    incorrectGuess.clear()
    correctGuesses.clear()


def main():
    word, hints = setUpGame()
    drawGameScreen(word, None)

    while True:
        char = input('\nType a letter or ask for a hint: ')
        valid = checkIfCharIsValid(char)

        while not valid:
            char = input('\nInvalid. Type a letter or ask for a hint: ')
            valid = checkIfCharIsValid(char)

        char = char.upper()
        if char == 'HINT':
            hint = chooseRandomHint(hints)
            drawGameScreen(word, hint)
        elif char == 'ESC':
            break
        else:
            if checkIfCharWasUsed(char, usedLettersArr):
                hint = 'You\'ve already typed this letter.'
                drawGameScreen(word, hint)
            else:
                usedLettersArr.append(char)
                if checkIfCharIsCorrect(char, word):
                    correctGuesses.append(char)
                    drawGameScreen(word, None)
                else:
                    incorrectGuess.append(char)
                    drawGameScreen(word, None)
        if checkIfGameIsOver(correctGuesses, word):
            drawEndScreen()
            clearAllArrays()
            word, hints = setUpGame()
            drawGameScreen(word, None)


main()
