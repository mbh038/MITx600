# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 14:07:32 2015

@author: Mike
"""
import random
import pylab



## PROBLEM 2-1

## Normal Simulations

def makeNormal(mean, sd, numSamples,title=None):
    samples = []
    for i in range(numSamples):
        samples.append(random.gauss(mean, sd))
    pylab.figure() 
    if title != None:
        pylab.title(title)
    pylab.hist(samples, bins = 10)
    #pylab.xlim((-20,20))
    #pylab.ylim((-15,15))

makeNormal(0, 3.0, 1000,"A")
makeNormal(0, 5.0, 1000,"B")
pylab.show()