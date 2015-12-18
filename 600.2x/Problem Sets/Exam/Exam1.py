# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 15:07:46 2015

@author: Mike
"""
#import pylab
#a = 1.0
#b = 2.0
#c = 4.0
#yVals = []
#xVals = range(-20, 20)
#for x in xVals:
#    yVals.append(a*x**2 + b*x + c)
#yVals = 2*pylab.array(yVals)
#xVals = pylab.array(xVals)
#try:
#    a, b, c, d = pylab.polyfit(xVals, yVals, 3)
#    print a, b, c, d
#except:
#    print 'fell to here'
        
        
#def getMeanAndStd(X):
#    mean = sum(X)/float(len(X))
#    tot = 0.0
#    for x in X:
#        tot += (x - mean)**2
#    std = (tot/len(X))**0.5
#    return mean, std
#    
#A= [0,1,2,3,4,5,6,7,8]
#
#B= [5,10,10,10,15]
#
#C= [0,1,2,4,6,8]
#
#D= [6,7,11,12,13,15]
#
#E= [9,0,0,3,3,3,6,6]
#
#
#print "A:", getMeanAndStd(A)
#print "B:", getMeanAndStd(B)
#print "C:", getMeanAndStd(C)
#print "D:", getMeanAndStd(D)
#print "E:", getMeanAndStd(E)
#
#
#def possible_mean(L):
#    return sum(L)/len(L)
#
#def possible_variance(L):
#    mu = possible_mean(L)
#    temp = 0
#    for e in L:
#        temp += (e-mu)**2
#    return temp / len(L)
#    
#print "A:", possible_variance(A)
#print "B:", possible_variance(B)
#print "C:", possible_variance(C)
#print "D:", possible_variance(D)
#print "E:", possible_variance(E)


def mysteryLinkageDist(self, other):
        av_dist = self.averageLinkageDist(other)
        max_dist = self.maxLinkageDist(other)
        min_dist = self.singleLinkageDist(other)
        retDist = 0.0
        if av_dist == max_dist and max_dist == min_dist:
            retDist = av_dist
        elif av_dist == max_dist:
            retDist = av_dist
        elif av_dist == min_dist:
            retDist = av_dist
        elif max_dist == min_dist:
            retDist = min_dist
        else:
            retDist = random.choice([av_dist,min_dist,max_dist])
        return retDist