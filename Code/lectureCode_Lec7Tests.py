def isPal(x):
    assert type(x) == list
    temp = x[:]
    print (temp,x)
    temp.reverse()
    print (temp,x)
    if temp == x:
        return True
    else:
        return False

def silly(n):
    result = []
    for i in range(n): 
        elem = raw_input('Enter element: ')
        result.append(elem)
        # print result
    if isPal(result):
        print('Yes')
    else:
        print('No')
