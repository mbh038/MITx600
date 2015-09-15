def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    return base*recurPower(base,exp-1)
        
def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    if exp == 0:
        return 1
    if exp % 2 == 0:
        return  recurPowerNew(base*base,exp/2)
    else:
        return base*recurPowerNew(base,exp-1)

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    smallest=min(a,b)
    largest=max(a,b)

    test=min(a,b)
    while test >= 1:
        if largest % test == 0 and smallest % test == 0:
            return test
        else:
            test -=1
    return 1

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == 0:
        return b
    if b == 0:
        return a
    return gcdRecur(b,a % b)

# Towers of Hanoi - one base case, two recursive cases

def printMove(fr, to):
    '''
    Towers of Hanoi
    '''
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    '''
    Towers of Hanoi
    '''
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

# Fibonacci - two bases cases, one recursive case

def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    assert type(x) == int and x >= 0
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
   

 # Palindromes - recursion with strings

def isPalindrome(s):
     
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))


#L5 Problem 6 - iterative

def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    n=0
    for c in aStr:
        n+=1
    return n

#L5 Problem 7 - recursive

def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    if aStr=="":
        return 0
    return 1+lenRecur(aStr[0:-1])
    
# L5 Problem 8 - bisection search

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    a=False
    s=sorted(aStr)
    print s
    mid=int(len(s)/2)
    #print mid,s[mid]
          
    if char == s[mid]:
        print char,mid,s[mid]
        return True

    if char < s[mid]:
        s=s[:mid]
        isIn(char,s)
        return False
    elif char > s[mid]:
        s=s[mid:]
        isIn(char,s)
        return False

     

        
    
