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

    def setFrob(middleFrob,beforeFrob=None,afterFrob=None):
        """
        each argument is a Frob.
        sets the before and after of middleFrob.
        resets the before and after of the frobs either side of middleFronb
        if the y exist. 
        """
        if afterFrob:
                middleFrob.setAfter(afterFrob)
                afterFrob.setBefore(middleFrob)
        if beforeFrob:
                middleFrob.setBefore(beforeFrob)
                beforeFrob.setAfter(middleFrob)
    
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
    print "First frob: " + str(firstFrob.myName())
    lastFrob=findLast(atMe)
    print "Last frob: " + str(lastFrob.myName())
    
    # if name is same as atMe, put it after atMe
    if newFrob.myName() == atMe.myName():
        print "same as atMe: " +str(newFrob.myName())+", atMe=: " +str(atMe.myName())
        setFrob(newFrob,atMe,atMe.getAfter())

    # if name is beyond the end of the list, put it at the end
    elif newFrob.myName() >= lastFrob.myName():
        print "at end: " +str(newFrob.myName())+", atMe=: " +str(atMe.myName())
        setFrob(newFrob,lastFrob,None)

    # if name is before the beginning of the list, put it at the front
    elif newFrob.myName() <= firstFrob.myName():
        print "at start: " +str(newFrob.myName())+", atMe=: " +str(atMe.myName())
        setFrob(newFrob,None,firstFrob)

    # if after atMe but before the end...
    elif newFrob.myName() > atMe.myName() and   newFrob.myName() <lastFrob.myName():
        print "after atme: " +str(newFrob.myName())+", atMe=: " +str(atMe.myName())
        temp=atMe.getAfter()
        while temp.getAfter():
            if newFrob.myName()<= temp.myName():
                setFrob(newFrob,temp.getBefore(),temp)
                break
            temp=temp.getAfter()
                
    # if before atMe but after the beginning...
    elif newFrob.myName() < atMe.myName() and   newFrob.myName() > firstFrob.myName():
        print "before atme: " +str(newFrob.myName())+", atMe=: " +str(atMe.myName())
        temp=atMe.getBefore()
        while temp.getBefore():
            if newFrob.myName()>= temp.myName():
                setFrob(newFrob,temp,temp.getAfter())
                break
            temp=temp.getBefore()   

# Test

# to be put in an ordered doubly linked list
eric = Frob('Eric')
andrew = Frob('Andrew')
ruth = Frob('Ruth')
fred = Frob('Fred')
martha = Frob('Martha')

john1=Frob("John")
john2=Frob("John")
john3=Frob("John")
john4=Frob("John")
john5=Frob("John")

# not in the list
abby=Frob("Abby") # before the first of the list
zoe=Frob("Zoe") # after the last of the list
eric2=Frob("Eric") # same name as one of the frobs in the list
paul=Frob("Paul") # somewhere in the middle of the list
john=Frob("John")
blanca=Frob("")

# set up the double linked list, ordered alphabetically
andrew.setAfter(eric)
eric.setBefore(andrew)
eric.setAfter(fred)
fred.setBefore(eric)
fred.setAfter(martha)
martha.setBefore(fred)
martha.setAfter(ruth)
ruth.setBefore(martha)

# a list in which all the names are the same
john1.setAfter(john2)
john2.setBefore(john1)
john2.setAfter(john3)
john3.setBefore(john2)
john3.setAfter(john4)
john4.setBefore(john3)
john4.setAfter(john5)
john5.setBefore(john4)



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

##
##    # Show the linked list 
##front = find_front(eric)
##show_tree(front) # andrew eric fred martha martha ruth
    
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
