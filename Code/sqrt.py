x = 23
epsilon = 0.01
step = 0.001
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break
    print guess
if abs(guess**2 - x) >= epsilon:
    print 'failed'
    print guess
else:
    print 'succeeded: ' + str(guess)