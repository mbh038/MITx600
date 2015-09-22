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
   # Base case: If aStr is empty, we did not find the char.
   if aStr == '':
      return False

   # Base case: if aStr is of length 1, just see if the chars are equal
   if len(aStr) == 1:
      return aStr == char

   # Base case: See if the character in the middle of aStr equals the 
   #   test character 
   midIndex = len(aStr)/2
   midChar = aStr[midIndex]
   if char == midChar:
      # We found the character!
      return True
   
   # Recursive case: If the test character is smaller than the middle 
   #  character, recursively search on the first half of aStr
   elif char < midChar:
      return isIn(char, aStr[:midIndex])

   # Otherwise the test character is larger than the middle character,
   #  so recursively search on the last half of aStr
   else:
      return isIn(char, aStr[midIndex+1:])
      
#L5 Problem 6 - use of wrapper function

def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)
    
def semordnilap(str1,str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    
    # Base case: if strings are of unequal length they cannot be semordnilap
    if len(str1) != len(str2):
        return False
    
    #Base case: If first character of str1 is not the same as the last character
    # of str2,they are not semordnilap
    if str1[0] != str2[-1]:
        return False
        
        # Base case: If strings are both of length 1, they are semordnilap
    if len (str1) == 1 and len(str2) == 1:
        if str1==str2:
            return True
        else:
            return False
    
            
    # Recursive case: first character of str1 is same as last character of
    # str2, recursively check this

    return semordnilap(str1[1:],str2[:-1])
