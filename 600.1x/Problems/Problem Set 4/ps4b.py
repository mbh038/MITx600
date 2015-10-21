from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore=0
    nValid=0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord="None"
    # For each word in the wordList
    for newWord in wordList:

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(newWord,hand,wordList):
            nValid += 1
            # Find out how much making that word is worth
            newScore=getWordScore(newWord, n)

            # If the score for that word is higher than your best score
            if newScore > maxScore:

                # Update your best score, and best word accordingly
                bestWord=newWord
                maxScore=newScore


    # return the best word you found.

    return bestWord

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    score =0
    newHand=hand.copy()
    # calculate hand length
    handLen=n

    while handLen > 0:
    # As long as there are still letters left in the hand:
 
        # Display the hand
        displayHand(newHand)

        # Ask computer for input
        word=compChooseWord(newHand, wordList, handLen)

        # If the input is a single period:

        if word =="None":
            print ("Total score: " + str(score)+ " points")
            # End the game (break out of the loop)
            return

        # Otherwise (the input is not a single period):

        else:
            score += getWordScore(word, n)

            # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            print ("'"+word+"'"+" earned "+str(getWordScore(word, n))+" points. Total: "+str(score)+" points")
            print

            # Update the hand
            newHand=updateHand(newHand, word)
            handLen=calculateHandlen(newHand)
                      
    # Game is over (user entered 'None' or ran out of letters), so tell user the total score
    print ("Total score: " + str(score)+ " points")
    return
    

# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    ngame=0
    while 1 > 0:
        print
        game=raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if game == "e":
            return
        elif game=="r":
            if ngame==0:
                print("You have not played a hand yet. Please play a new hand first!")
                continue
            else:
                player ="x"
                while player != "u" and player != "c":
                    player=raw_input("Enter u for user, c for computer: ")
                    if player != "u" and player != "c":
                        print("Invalid command")
                if player == "u":
                    ngame +=1
                    playHand(hand, wordList, HAND_SIZE)
                elif player == "c":
                    ngame += 1
                    compPlayHand(hand, wordList, HAND_SIZE)
                else:
                    print("Invalid command.")
                    continue                    
        elif game=="n":
                player ="x"
                while player != "u" and player != "c":
                    player=raw_input("Enter u for user, c for computer: ")
                    if player != "u" and player != "c":
                        print("Invalid command")
                if player == "u":
                    ngame +=1
                    hand=dealHand(HAND_SIZE)
                    playHand(hand, wordList, HAND_SIZE)
                elif player == "c":
                    ngame += 1
                    hand=dealHand(HAND_SIZE)
                    compPlayHand(hand, wordList, HAND_SIZE)
                else:
                    print("Invalid command.")
                    continue
        else:
            print("Invalid command.")
            continue
        
    #print "playGame not yet implemented." # <-- Remove this when you code this function

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


