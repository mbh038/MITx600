# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 16:20:36 2015

@author: michael.hunt
"""

# L2 Simulation and Random Walks
import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    # Your code here
    return random.randrange(0, 100, 2)
    

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    # Your code here
    random.seed(123)
    return random.randrange(10,22,2)
    
    
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    # Your code here
    return random.randrange(10,22,2)
    
def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1 