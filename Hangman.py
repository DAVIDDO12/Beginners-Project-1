import random
HMpics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]
words = ["code", "python", "program", "computer", "variable", "module", "string", "input", "output", "iteration", "set", "subroutine", "boolean", "data", "list", "function", "operator", "parameter", "statement", "repository"]
def hangman():
    word = random.choice(words)
    guessedletters = []
    correctletters = [''] * len(word)
    attempts = 0
    maxattempts = len(HMpics) - 1
    while attempts < maxattempts and ''.join(correctletters) != word:
        print(HMpics[attempts])
        print(' '.join(correctletters))
        print("Letters guessed:", ' '.join(guessedletters))
        guess = input("Guess a letter: ").lower()
        if guess in guessedletters:
            print("You already guessed that!")
            continue
        guessedletters.append(guess)
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    correctletters[i] = guess
        else:
            print("Nope")
            attempts += 1
    if ''.join(correctletters) == word:
        print("You got it!")
        print("The word was:", (word))
    else:
        print(HMpics[attempts])
        print("He died rip :(")
        print("The word was:", (word))
hangman()
