# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 21:51:24 2015

@author: Mike
"""



##DRUNK VARIATIONS

##Here are several different variations on a drunk.

import pylab
import random
import math

class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
        
    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Field(object):
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name
 

#NEW CODE

#The following function is new, and returns the actual x and y distance
# from the start point to the end point of a random walk.

def walkVector(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(f.getLoc(d).getX() - start.getX(),
           f.getLoc(d).getY() - start.getY())
 

##DRUNK VARIATIONS

##Here are several different variations on a drunk.

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,0.9), (0.0,-1.03), (1.03, 0.0), (-1.03, 0.0)]
        return random.choice(stepChoices)

class EDrunk(Drunk):
    def takeStep(self):
        ang = 2 * math.pi * random.random()
        length = 0.5 + 0.5 * random.random()
        return (length * math.sin(ang), length * math.cos(ang))

class PhotoDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.0, 0.5),(0.0, -0.5),
                     (1.5, 0.0),(-1.5, 0.0)]
        return random.choice(stepChoices)

class DDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.85, 0.85), (-0.85, -0.85),
                     (-0.56, 0.56), (0.56, -0.56)] 
        return random.choice(stepChoices)
        
def drunkWalk(d,numSteps):
    f=Field()    
    origin=Location(0,0)
    f.addDrunk(d,origin)
    endpoint=[]
    x=[]
    y=[]
    for i in range(numSteps):
        endpoint.append(walkVector(f, d, numSteps))
        x.append(endpoint[i][0])
        y.append(endpoint[i][1])
    pylab.plot(x,y,marker='.', linestyle="None") 
    pylab.xlim((-100,100))
    pylab.ylim((-100,100))
    pylab.show()
        
pylab.title("UsualDrunk")
d=UsualDrunk("John")    
drunkWalk(d,1000)
pylab.title("ColdDrunk")
d=ColdDrunk("John")    
drunkWalk(d,1000)
pylab.title("EDrunk")
d=EDrunk("John")    
drunkWalk(d,1000)
pylab.title("PhotoDrunk")
d=PhotoDrunk("John")    
drunkWalk(d,1000)
pylab.title("DDrunk")
d=DDrunk("John")    
drunkWalk(d,1000)