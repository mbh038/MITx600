## Doubly Linked List

## MITx600.1x Exam

## Problem 6-1

class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
    
def findFirst(atMe):
    """
    atMe: a Frob that is part of a doubly linked list
    returns the frob at the front of the list
    """
    temp=atMe
    while temp.getBefore():
        temp=temp.getBefore()
    return temp
        
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links
    This procedure appropriately inserts newFrob into the linked list that
    atMe is a part of.    
    """
    # Your Code Here

    def setFrob(middleFrob,previousFrob=None,nextFrob=None):
        """
        each argument is a Frob.
        sets the before and after of middleFrob.
        resets the before and after of the frobs either side of middleFronb
        if the y exist. 
        """
        if nextFrob:
                middleFrob.setAfter(nextFrob)
                nextFrob.setBefore(middleFrob)
        if previousFrob:
                middleFrob.setBefore(previousFrob)
                previousFrob.setAfter(middleFrob)
    
    def findFirst(atMe):
        """
        atMe: a Frob that is part of a doubly linked list
        returns the frob at the front of the list
        """
        temp=atMe
        while temp.getBefore():
            temp=temp.getBefore()
        return temp

    def findLast(atMe):
        """
        atMe: a Frob that is part of a doubly linked list
        returns the frob at the end of the list
        """
        temp=atMe
        while temp.getAfter():
            temp=temp.getAfter()
        return temp

    # identify the first and last Frobs in the list
    firstFrob=findFirst(atMe)
    lastFrob=findLast(atMe)
    
    # if name is same as atMe, put it after atMe
    if newFrob.myName() == atMe.myName():
        setFrob(newFrob,atMe,atMe.getAfter())

    # if name is beyond the end of the list, put it at the end
    elif newFrob.myName() >= lastFrob.myName():
        setFrob(newFrob,lastFrob,None)

    # if name is before the beginning of the list, put it at the front
    elif newFrob.myName() <= firstFrob.myName():
        setFrob(newFrob,None,firstFrob)

    # if after atMe but before the end...
    elif newFrob.myName() > atMe.myName() and   newFrob.myName() <lastFrob.myName():
        temp=atMe.getAfter()
        while temp:
            if newFrob.myName()<= temp.myName():
                setFrob(newFrob,temp.getBefore(),temp)
                break
            temp=temp.getAfter()
                
    # if before atMe but after the beginning...
    elif newFrob.myName() < atMe.myName() and   newFrob.myName() > firstFrob.myName():
        temp=atMe.getBefore()
        while temp:
            if newFrob.myName()>= temp.myName():
                setFrob(newFrob,temp,temp.getAfter())
                break
            temp=temp.getBefore()   

def findFirst(atMe):
    """
    atMe: a Frob that is part of a doubly linked list
    returns the frob at the front of the list
    """
    temp=atMe
    while temp.getBefore():
        temp=temp.getBefore()
    return temp

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    if start.getBefore():
        return findFront(start.getBefore())
    else:
        return start

def findEnd(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the end of the linked list 
    """
    if start.getAfter():
        return findEnd(start.getAfter())
    else:
        return start

def WalkListForward(node):
    print "## Walking the list forward ##"
    temp = findFront(node)
    while temp:
        print temp.myName()
        temp = temp.getAfter()
        
def WalkListBackward(node):
    print "## Walking the list backward ##"
    temp = findEnd(node)
    while temp:
        print temp.myName()
        temp = temp.getBefore()

## Testing ##

print
print "Test 2"
test_list=Frob("gabby")
insert(test_list, Frob("allison"))
print ""
WalkListForward(test_list)
print ""
WalkListBackward(test_list)


print
print "Test 2"
test_list=Frob("gabby")
insert(test_list, Frob("zara"))
print ""
WalkListForward(test_list)
print ""
WalkListBackward(test_list)

print
print "Test 3"
test_list = Frob('abby')
insert(test_list, Frob("xander"))
insert(test_list, Frob("beto"))
print ""
WalkListForward(test_list)
print ""
WalkListBackward(test_list)

print
print "Test 4"
test_list=Frob("alvin")
insert(test_list, Frob("alvin"))
print ""
WalkListForward(test_list)
print ""
WalkListBackward(test_list)

print
print "Test 5"
test_list = Frob('allison')
insert(test_list, Frob("lyla"))
insert(test_list, Frob("christina"))
insert(test_list, Frob("ben"))
print ""
WalkListForward(test_list)
print ""
WalkListBackward(test_list)

print
print "Test 6"
test_list = Frob('zsa zsa')
a = Frob('ashley')
m = Frob('marcella')
v = Frob('victor')
insert(test_list, m)
insert(m, a)
insert(a, v)
print ""
WalkListForward(test_list)
print ""
WalkListBackward(test_list)

print
print "Test 7"
test_list = Frob('mark')
c = Frob('craig')
insert(test_list, Frob("sam"))
insert(test_list, Frob("nick"))
insert(test_list, c)
insert(c, Frob("xanthi"))
insert(test_list, Frob("jayne"))
insert(c, Frob("martha"))
print ""
WalkListForward(c)
print ""
WalkListBackward(c)

print
print "Test 8"
test_list = Frob('leonid')
a = Frob('amara')
j1 = Frob('jennifer')
j2 = Frob('jennifer')
s = Frob('scott')
insert(test_list, s)
insert(s, j1)
insert(s, j2)
insert(j1, a)
print ""
WalkListForward(test_list)
print ""
WalkListBackward(test_list)

print
print "Test 9"
test_list = Frob('eric')
insert(test_list, Frob("eric"))
insert(test_list, Frob("chris"))
insert(test_list, Frob("john"))
insert(test_list, Frob("john"))
insert(test_list, Frob("chris"))
insert(test_list, Frob("eric"))
insert(test_list, Frob("john"))
insert(test_list, Frob("chris"))
print ""
WalkListForward(test_list)
print ""
WalkListBackward(test_list)
