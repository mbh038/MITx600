# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.
    import string
    dlc = dict.fromkeys(string.ascii_lowercase, 0)
    duc = dict.fromkeys(string.ascii_uppercase, 0)
    # create upper  case cipher
    for letter in duc.keys():
        index=string.ascii_uppercase.index(letter)
        index=index+shift
        if index >= 26:
            index -=26
        duc[letter]=string.ascii_uppercase[index]
    # create upper case ciper
    for letter in dlc.keys():
        index=string.ascii_lowercase.index(letter)
        index=index+shift
        if index >= 26:
            index -=26
        dlc[letter]=string.ascii_lowercase[index]
    # join them   
    dcc=dict(dlc.items()+duc.items())
    return dcc 

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO.
    newText=""
    for letter in text:
        if letter in coder.keys():
            newText += coder[letter]
        else:
            newText += letter
    
    return newText

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.

    return applyCoder(text,buildCoder(shift))

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO - with pseudocode included!
    # split text into list of words
    textWords=text.split(" ")
    for word in textWords:
        word=word.strip("0123456789") # remove any lingering digits
    # set counter list to zero
    counter=[0]*26
    # for each possible shift key 0 to 25...
    for i in range(len(counter)):     
        for word in textWords:
            # for each word in textWords, shift it by the shift key 
            shiftedWord=applyShift(word,i)
            # is it a valid word
            if isWord(wordList, shiftedWord) == True:
                counter[i]+=1
    # which counter element is the biggest?
    max_value = max(counter)
    max_index = counter.index(max_value)
    # return best guess at shift key
    return max_index

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    wordList=loadWords()
    CodedStory=getStoryString()
    bestShift=findBestShift(wordList,CodedStory)
    deCodedStory=applyShift(CodedStory,bestShift)
    return deCodedStory

# The decoded story is:
# 'Jack Florey is a mythical character created on the spur of a moment to help
# cover an insufficiently planned hack. He has been registered for classes at MIT
# twice before, but has reportedly never passed a class. It has been the
# tradition of the residents of East Campus to become Jack Florey for a few
# nights each year to educate incoming students in the ways, means, and ethics
# of hacking.\n'   

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    # wordList = loadWords()
    # s = applyShift('Hello, world!', 8)
    # bestShift = findBestShift(wordList, s)
    # assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
   decryptStory()
