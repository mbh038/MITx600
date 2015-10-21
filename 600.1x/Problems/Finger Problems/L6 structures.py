def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    oddTup=()
    counter = 0
    for i in range(0,len(aTup)):
        if i % 2 == 0:
            oddTup =oddTup + (aTup[i],)
    return oddTup
    
    