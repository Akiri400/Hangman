# Problem Set 2, hangman.py
# Name: Ahmed Mohamed
# Collaborators: None
# Time spent: Time

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    confirmed_letters = []
    for char1 in secret_word:
        for char2 in letters_guessed:
            if char1 == char2:
                confirmed_letters += char2
                break
    str_confirmed_letters = "".join(confirmed_letters)
    return secret_word == str_confirmed_letters



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = []
    for char1 in secret_word:
        for char2 in letters_guessed:
            if char1 == char2 and char1 == secret_word[-1]:
                guessed_word += char2
                break
            elif char1 == char2:
                guessed_word += char2 + " "
                break
        else:
            if char1 == secret_word[-1]:
                guessed_word += "_"
            else:
                guessed_word += "_ "

    guessed_word2 = "".join(guessed_word)
    return guessed_word2


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    import string
    alphabet = string.ascii_lowercase
    alphabet2 = list(alphabet)
    not_guessed = []
    for letter in alphabet2:
        for letter2 in letters_guessed:
            if letter == letter2:
                break
        else:
            not_guessed += letter
    not_guessed2 = "".join(not_guessed)
    return not_guessed2


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * 1) At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * 2) The user should start with 6 guesses

    * 3) Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * 4) Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * 5) The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * 6) After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    v = 0
    vowel = "aeiou"
    warning = 3
    letters_guessed = []
    n_letters = len(secret_word)
    n_guesses = 6
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(n_letters) + " letters long.")
    print("-----------")
    for x in range(n_guesses):
        z = 0
        if int(n_guesses-x-v) < 1:
            break
        if is_word_guessed(secret_word, letters_guessed) == True:
            print("Well done, you WON!")
            break
        if warning < 0:
            print("You have no more warnings")
        else:
            print("You have", warning, "warnings left.")
        print("You have", n_guesses-x-v, "guesses left.")
        print("Available letters: ", get_available_letters(letters_guessed))
        one_letter = (input("Please guess a letter: "))
        lower_one_letter = str.lower(one_letter)

        # IF GUESS IS NEW AND CORRECT
        while (lower_one_letter not in letters_guessed) and (lower_one_letter in secret_word):
            letters_guessed += list(lower_one_letter)
            print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
            print("-----------")
            if is_word_guessed(secret_word, letters_guessed) == True:
                break
            if warning < 0:
                print("You have no more warnings")
            else:
                print("You have", warning, "warnings left.")
            print("You have", n_guesses-x-v, "guesses left.")
            print("Available letters: ", get_available_letters(letters_guessed))
            one_letter = (input("Please guess a letter: "))
            lower_one_letter = str.lower(one_letter)

        # IF THE GUESS HAS ALREADY BEEN GUESSED BEFORE
        while lower_one_letter in letters_guessed and lower_one_letter in string.ascii_lowercase:
            warning -= 1
            if warning < 0:
                {
                    print("Oops! You have already guessed this letter. You have lost a guess:",
                            get_guessed_word(secret_word, letters_guessed))
                }
                z = 1
                break
            if warning >= 0:
                {
                    print("Oops! You have already guessed this letter. You have", warning, "warnings left:",
                            get_guessed_word(secret_word, letters_guessed))
                }
            one_letter = (input("Please guess a letter: "))
            lower_one_letter = str.lower(one_letter)

        # IF THE GUESS IS NOT A VALID CHARACTER (NOT A UPPER OR LOWERCASE ALPHABET CHAR)
        while str.isalpha(lower_one_letter) == False:
                warning -= 1
                if warning < 0:
                    {
                    print("Oops! That is not a valid letter. You have lost a guess:",
                          get_guessed_word(secret_word, letters_guessed))
                    }
                    break
                if warning >= 0:
                    {
                    print("Oops! That is not a valid letter. You have", warning, "warnings left:",
                        get_guessed_word(secret_word, letters_guessed))
                    }
                one_letter = (input("Please guess a letter: "))
                lower_one_letter = str.lower(one_letter)

        letters_guessed += list(lower_one_letter)

        # TEST IF USER HAS GUESSED THE WORD CORRECTLY
        if is_word_guessed(secret_word, letters_guessed) == True:
            print("Well done, you WON!")
            break

        # IF THE USER HAS MADE A VALID INCORRECT GUESS
        if lower_one_letter not in secret_word and lower_one_letter in string.ascii_lowercase and z == 0:
            if lower_one_letter in vowel:
                v += 1
            print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
        print("-----------")

    # REVEALS SECRET WORD IF USER HAS USED UP ALL GUESSES
    if is_word_guessed(secret_word, letters_guessed) == False:
        print("The right answer was: ", secret_word)



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
