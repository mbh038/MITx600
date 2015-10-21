# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
letters=["d","e","a","v"]

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    guessed = 0
    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] in secretWord:
            guessed +=1
    if guessed == len(secretWord):
        return True
    else:
        return False
        

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    opString=''
    for char in secretWord:
        if char in lettersGuessed:
            opString=opString+char
        else:
            opString=opString+("_ ")
    return opString



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    notPresent=''
    alphabet=string.ascii_lowercase

    for char in alphabet:
        if not char in lettersGuessed:
            notPresent=notPresent+char
    return notPresent
  
def nLetter(secretWord,guess):
    '''
    secretWord: string, word to be guessed
    guess: string, letter guess
    returns: int, number of times that guess appears in secretword.
    '''
    n=0
    for char in secretWord:
        if guess == char:
            n +=1
    return n
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    secretWord=secretWord.lower()
    length=len(secretWord)
    lettersLeft=string.ascii_lowercase
    lettersGuessed=[]

    print("Welcome to the game of hangman!")
    print("I am thinking of a word that is "+str(length)+" letters long.")

    nGuessLeft=8

    while nGuessLeft > 0:
        print("-------------")
        print("You have "+str(nGuessLeft)+" guesses left")
        
        print("Available Letters: " + lettersLeft)
        guess=raw_input("Please guess a letter: ")
        guess=guess.lower()


        if guess in secretWord:         
            if guess in lettersLeft:
                lettersGuessed.append(guess)
                lettersLeft=getAvailableLetters(lettersGuessed)
                print("Good guess: "),
                print getGuessedWord(secretWord, lettersGuessed)

                if nLetter(secretWord,guess) > 1:
                    for i in range(nLetter(secretWord,guess)-1):
                        lettersGuessed.append(guess)

                if isWordGuessed(secretWord, lettersGuessed)==True:
                    print("-------------")
                    print "Congratulations, you won!"
                    return
                    
                    
            else:
                
                print("Oops! You've already guessed that letter: "),
                print getGuessedWord(secretWord, lettersGuessed)

        else:          
            if guess in lettersLeft:
                nGuessLeft -=1
                lettersGuessed.append(guess)
                lettersLeft=getAvailableLetters(lettersGuessed)
                print("Oops! That letter is not in my word: "),
                print getGuessedWord(secretWord, lettersGuessed)
            else:
                print("Oops! You've already guessed that letter: "),
                print getGuessedWord(secretWord, lettersGuessed)              

    print("-------------")
    print "Sorry, you ran out of guesses. The word was " + secretWord+"."
    return

          




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
