# Quiz

# 4 Part 1

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a*x**2 + b*x + c

# 4 Part 2

def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    result=evalQuadratic(a1, b1, c1, x1)+evalQuadratic(a2, b2, c2, x2)
    print result
    return

# 5 Find primes below n

def primesList(N):
    '''
    N: an integer
    '''
    a=[True for i in range(1,N+2)]
    op=[]
    limit = int(N**0.5)

    for i in range (2,limit+1):
        #print i
        if a[i]==True:
            j=0
            while i**2 + j*i<=N:
                #print "i: " + str(i) +", j: "+ str(j)+ ", i^2 +ji: "+ str(i**2 + j*i)
                test=i**2+j*i
                a[test]=False
                j +=1
    for i in range(2,N+1):
        if a[i] == True:
            op.append(i)
            #print i,
    # print op
    return op

def testPrimes (N):
    for i in range (N+1):
        print str(i)+": ",
        print primesList(i)


# 6 - Counting number of occurrences of digit 7 in a non-negative integer N

# using recursion

def count7(N):
    '''
    MUST use recursion
    N: a non-negative integer
    '''

    if N%10 == 0 and N < 10:
        return 0
    else:
        if N%10==7:
            return 1+ count7(N/10)
        else:
            return count7(N/10)

# 7 Dictionaries

def uniqueValues(aDict):
    '''
    Returns a list of keys in aDict that map to integer values that are unique
    (i.e. values appear exactly once in aDict).

    aDict: a dictionary
    '''
    # Your code here

    counts=dict()
    vals=[]
    keys=[]
    uniqueVals=[]
    

    for key in aDict.keys():
        vals.append(aDict[key])
        keys.append(key)
    #print vals
    #print keys
    for val in vals:
        counts[val]=counts.get(val,0)+1
    #print counts
   
    for i in range (len(aDict)):
       if counts[vals[i]]==1:
           uniqueVals.append(keys[i])
    return sorted(uniqueVals)      


def testUd():

    testDicts=[
    {1: 1, 2: 2, 3: 3},
    {1: 1, 2: 1, 3: 1},
    {1: 1},
    {1: 1, 2: 1, 3: 3},
    {2: 2, 3: 3, 4: 4},
    {},
    {2: 0, 3: 3, 6: 1},
    {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0},
    {0: 9, 1: 1, 2: 7, 3: 3, 5: 2, 6: 5, 7: 8, 9: 10, 10: 0},
    {8: 3, 1: 3, 2: 2},
    {2: 2, 5: 0, 7: 3},
    {0: 3, 1: 2, 2: 3, 3: 1, 4: 0, 6: 0, 7: 4, 8: 2, 9: 7, 10: 0},
    {0: 2, 1: 3, 2: 0, 3: 6, 7: 2, 9: 3},
    {8: 1, 0: 4, 1: 1, 5: 2, 9: 4}]

    print len(testDicts)

    for i in range(len(testDicts)):
        uniqueValKeys=uniqueValues(testDicts[i])
        print uniqueValKeys
        
    
# 8 String Mutation

#try a variey of f functions
def f(s):
    return s!=""

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    # Your function implementation here
    tf=[]
    for i in range(len(L)):
        tf.append(f(L[i]))


    count=0
    for i in range(len(tf)):
        if tf[i] == False:
            del L[i-count]
            count +=1
    return len(L)

def test_satisfiesF():

    testL=[
        [],
        ["a","",""],
        ["aa","a"],
        ["b"],
        ["b","b"]
        ]
      
    for i in range(len(testL)):
        print testL[i],
        print satisfiesF(testL[i]),
        print testL[i]






    
            
