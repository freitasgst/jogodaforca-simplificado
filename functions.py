import random


# RED   = "\033[1;31m"
# CYAN  = "\033[1;36m"
# GREEN = "\033[0;32m"
# RESET = "\033[0;0m"


def setUpGame():
    words = readGameFile()
    rword = chooseRandomWord(words)
    hints = selectAllHints(words, rword)
    rword = rword[2:].strip().upper()
    return rword, hints


def readGameFile():
    file = open('game.txt', 'r', encoding='utf-8')
    words = file.readlines()
    file.close()
    return words


def chooseRandomWord(words):
    palavra = random.choice(words)
    while 'D:' in palavra:
        palavra = random.choice(words)
    return palavra


def selectAllHints(words, word):
    dicas = []
    for i in range(len(words)):
        if (words[i] == word):
            k = i + 1
            while 'D:' in words[k]:
                dicas.append(words[k][2:].strip())
                k += 1
                if (k == len(words)):
                    break
    return dicas


def checkIfCharIsValid(char):
    if (not char.isalpha() or (len(char) != 1 and char.upper() != 'HINT')):
        return False
    return True


def checkIfGameIsOver(guesses, word):
    setword = set(word)
    guesses = set(guesses)
    if len(setword.difference(guesses)) == 0:
        return True
    return False


def chooseRandomHint(hints):
    return random.choice(hints)[2:]


def checkIfCharWasUsed(char, usedLettersArr):
    if char in usedLettersArr:
        return True


def checkIfCharIsCorrect(char, word):
    if char in word:
        return True
    return False
