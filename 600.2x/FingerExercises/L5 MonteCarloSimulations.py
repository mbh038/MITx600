# -*- coding: utf-8 -*-
"""
Created on Sat Nov 07 16:23:45 2015

@author: michael.hunt
"""
import random

def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])
    
def pickColour(nRed=3,nGreen=3):
    reds=[1]*nRed
    greens=[0]*nGreen
    balls=reds+greens
    return random.choice(balls)
    
def allTheSame(reds=3,greens=3,picks=3):

    picked=[]
    for i in range(picks):
        nextPicked=pickColour(reds,greens)
        picked.append(nextPicked)
        if nextPicked == 1:
            reds -=1
        elif nextPicked == 0:
            greens -=1
    if sum (picked) == 3 or sum (picked) == 0:
         return 1
    else:
         return 0
         
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    reds=3
    greens=3
    picks=3
    allSame=0
    for i in range(numTrials):
        allSame += allTheSame(reds,greens,picks)
    return float(allSame)/numTrials
 
noReplacementSimulation(1000)       