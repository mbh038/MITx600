# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 07:39:40 2015

@author: Mike
"""

import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    allSame=0
    for i in range(numTrials):
        bag=["r","r","r","r","g","g","g","g"]
        chosen=[]
        numChoose=3
         
       # choose first ball                        
        which=random.choice(range(len(bag)))
        chosen.append(bag[which])
        bag.pop(which)
        #print bag,chosen
        for j in  range(1,numChoose):
            which=random.choice(range(len(bag)))
            chosen.append(bag[which])
            bag.pop(which)
            if chosen[j] != chosen[j-1]:
                add = 0
                break
            else:
                add = 1
            #print bag,chosen
        allSame += add
        #print chosen
#    print allSame
    return float(allSame)/numTrials

    
numTrials=10000
a=drawing_without_replacement_sim(numTrials)