## DO NOT MODIFY THE IMPLEMENTATION OF THE Person CLASS ##
class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setAge(self, age):
        #assumes age is an int greater than 0
        #sets self's age to age (in years)
        self.age = age
    def getAge(self):
        #assumes that self's age has been set
        #returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        #return True if self's name is lexicographically less
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name
        
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self,name,status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        # Write your code here

        Person.__init__(self,name)
        if status =="citizen":
            self.status=status
        elif status =="legal_resident":
            self.status=status
        elif status =="illegal_resident":
            self.status=status
        else:
            raise ValueError ("%r is not a valid citizen status" % status)
        
    def getStatus(self):
        """
        Returns the status
        """
        # Write your code here
        if self.status =="citizen":
            return self.status
        elif self.status =="legal_resident":
            return self.status
        elif self.status =="illegal_resident":
            return self.status
        else:
            raise ValueError ("%r is not a valid citizen status" % self.status)


## Test
a1 = USResident('Tim Beaver', 'citizen')
print a1.getStatus()
a2 = USResident('Tim Carver', 'legal_resident')
print a2.getStatus()
a3 = USResident('Tim Donaldson', 'illegal_resident')
print a3.getStatus()
# b = USResident('Tim Horton', 'non-resident')
# print b.getStatus()
a1.setAge(67)
print a1.getAge()
print a1
print a1<a2
print a2>a3
a4=Person("Tim Evans")
a5=Person("Tim Folds")
print a4
print a5
print a4<a5
print a4>a5
a4.setAge(65)
print a4.getAge()
#print a5.getAge()
a6=USResident(" Tim ","citizen")
print a6
print a6.getStatus()
a7=USResident(" Tom ","citizen")
print a7
print a7.getStatus()
print a6<a7
a8=Person(" Tim ")
print a8


