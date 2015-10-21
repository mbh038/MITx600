# lecture 3.6
# bisection search for secret number

print('Please think of a number between 0 and 100!')

x = 100
numGuesses = 0
low = 0.0
high = x
ans = int((high + low)/2.0)
while True:
    numGuesses += 1
    print('Is your secret number ' +str(ans)+'?')
    response=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if response=="l":
        low = ans
    elif response=="h":
        high = ans
    elif response =='c':
        print ("Game over. Your secret number was: "+ str(ans))
        break
    else:
        print("Sorry, I did not understand your input.")
    ans = int((high + low)/2.0)
