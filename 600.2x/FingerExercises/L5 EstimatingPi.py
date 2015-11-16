# -*- coding: utf-8 -*-
"""
Created on Sat Nov 07 17:22:22 2015

@author: michael.hunt
"""
## Estimating Pi
import random

def buffonPi(numTrials,side):

    def randomPoint():
        x=side*(random.random()-0.5)
        y=side*(random.random()-0.5)
        return (x,y)
    
    inCircle=0
    for i in range(numTrials):
        newpoint=randomPoint()
        x=newpoint[0]
        y=newpoint[1]
        if x**2 + y**2 <= float(side**2)/4:
            inCircle +=1
    return 4.0*float(inCircle)/numTrials
    
print buffonPi(100000,2)