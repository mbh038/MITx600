animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    sum=0
    for a in aDict.keys():
        sum =sum+ len(aDict[a])
    return sum

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

test={'a': [16, 8, 3], 'c': [20, 13, 6, 3, 12, 16], 'b': [3, 19, 9, 7, 7, 18, 4], 'd': [20, 20, 20, 18, 2]}

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''

    if len(aDict) == 0:
        return
    biggest=len(aDict.values()[0])
    keyMax=aDict.keys()[0]
    for key in aDict.keys():
        if len(aDict[key]) >= biggest:
            keyMax= key
            biggest=len(aDict[key])
    return keyMax
    
