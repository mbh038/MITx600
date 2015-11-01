# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5
    
def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    lengths=[]
    if len(L)==0:
        return float('NaN')
    else:
        for i in range (len(L)):
            lengths.append(float(len(L[i])))
        return stdDev(lengths)
        
## Test cases

L1 = ['a', 'z', 'p']
stdDevOfLengths(L1)

L2 = ['apples', 'oranges', 'kiwis', 'pineapples']
stdDevOfLengths(L2)