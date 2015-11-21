# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std
    
    
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    #opdict={"Delay300":[],"Delay150":[],"Delay75":[],"Delay0":[]}
    opdict={"fp1":[],"fp2":[],"fp3":[],"fp4":[]}
    
# Vary the delay
#    fp1=simulationDTFinalPop(numTrials,300)
#    fp2=simulationDTFinalPop(numTrials,150)
#    fp3=simulationDTFinalPop(numTrials,75)
#    fp4=simulationDTFinalPop(numTrials,0)
    
# Vary number of viruses
#    fp1=simulationDTFinalPop(numTrials,150,50)
#    fp2=simulationDTFinalPop(numTrials,150,100)
#    fp3=simulationDTFinalPop(numTrials,150,200)
#    fp4=simulationDTFinalPop(numTrials,150,400)
    
# Vary maxPop
#    fp1=simulationDTFinalPop(numTrials,150,100,500)
#    fp2=simulationDTFinalPop(numTrials,150,100,1000)
#    fp3=simulationDTFinalPop(numTrials,150,100,2000)
#    fp4=simulationDTFinalPop(numTrials,150,100,4000)

# Vary maxBirthProb
   
#    fp1=simulationDTFinalPop(numTrials,150,100,1000,.1)
#    fp2=simulationDTFinalPop(numTrials,150,100,1000,.1)
#    fp3=simulationDTFinalPop(numTrials,150,100,1000,.1)
#    fp4=simulationDTFinalPop(numTrials,150,100,1000,.1)

# Vary clearProb
#    fp1=simulationDTFinalPop(numTrials,150,100,1000,.1,.025)
#    fp2=simulationDTFinalPop(numTrials,150,100,1000,.1,.05)
#    fp3=simulationDTFinalPop(numTrials,150,100,1000,.1,.1)
#    fp4=simulationDTFinalPop(numTrials,150,100,1000,.1,.2)

 #   print "Resistance to Gittagonol initially"
 #   fp1=simulationDTFinalPop(numTrials,150,100,1000,.1,.05,{"guttagonol": True})
 
    pylab.subplot(4, 1, 1)
    pylab.hist(fp1,bins=50)
    pylab.legend("1",loc="best")
    pylab.subplot(4, 1, 2)
    pylab.hist(fp2,bins=50)
    pylab.legend("2",loc="best")
    pylab.subplot(4, 1, 3)
    pylab.hist(fp3,bins=50)
    pylab.legend("3",loc="best")
    pylab.subplot(4, 1, 4)
    pylab.hist(fp4,bins=50)
    pylab.legend("4",loc="best")
    pylab.show()
    
    opdict["fp1"].append(fp1)
    opdict["fp2"].append(fp2)
    opdict["fp3"].append(fp3)
    opdict["fp4"].append(fp4)
    
    opdict["fp1"].append(sum(fp1)/len(fp1))
    opdict["fp2"].append(sum(fp2)/len(fp2))
    opdict["fp3"].append(sum(fp3)/len(fp3))
    opdict["fp4"].append(sum(fp4)/len(fp4))
    
    def propCured(finalPops):
        cured =0
        for popl in finalPops:
            if popl<=50:
                cured += 1
        return float(cured)/len(finalPops)
    
    opdict["fp1"].append(propCured(fp1))
    opdict["fp2"].append(propCured(fp2))
    opdict["fp3"].append(propCured(fp3))
    opdict["fp4"].append(propCured(fp4))   
    
    print "fp1: ",  opdict["fp1"][1],opdict["fp1"][2]
    print "fp2: ",  opdict["fp2"][1],opdict["fp2"][2]
    print "fp3: ",  opdict["fp3"][1],opdict["fp3"][2]
    print "fp4: ",  opdict["fp4"][1],opdict["fp4"][2]
    return opdict
    
#op=simulationDelayedTreatment(10)

def simulationDTFinalPop(numTrials,
                         delay,
                         numViruses=100,
                         maxPop=1000,
                         maxBirthProb=.1,
                         clearProb=.05,
                         resistances={"guttagonol": False},
                         mutProb=.005):

    timeSteps=list(range(delay+150))
#    popList=[0]*len(timeSteps)
    finalPop=[0]*numTrials
    #resList=[0]*len(timeSteps)
   
    for i in range(numTrials): #in patientList:

        virusList=[]
        for j in range(numViruses):   
           virusList.append(ResistantVirus(maxBirthProb,clearProb,resistances,mutProb))
        patient=TreatedPatient(virusList,maxPop)

        for j in timeSteps[:delay]:
            if patient.getTotalPop()>0:
                patient.update()
#                if resistances != {}:
#                    resList[j] += patient.getResistPop(resistances)
                
        patient.addPrescription('guttagonol')
     
        for j in timeSteps[delay:]:
            if patient.getTotalPop()>0:
                patient.update()
#                if resistances != {}:
#                    resList[j] += patient.getResistPop(resistances)    

        finalPop[i]=patient.getTotalPop()
        
    #pylab.hist(finalPop)
    #pylab.show()
    #print finalPop
    return finalPop
#    resList[:] = [float(x) / numTrials for x in resList]






#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    opdict={"fp1":[],"fp2":[],"fp3":[],"fp4":[]}
    
# Vary the delay
#    fp1=TDDFinalPop(numTrials,300)
#    fp2=TDDFinalPop(numTrials,150)
#    fp3=TDDFinalPop(numTrials,75)
#    fp4=TDDFinalPop(numTrials,0)
    
# Vary the mutProb
    fp1=TDDFinalPop(numTrials,150,100,1000,.1,.05,{"guttagonol": False, 'grimpex': False},.005)
    fp2=TDDFinalPop(numTrials,150,100,1000,.1,.05,{"guttagonol": False, 'grimpex': False},.05)
    fp3=TDDFinalPop(numTrials,150,100,1000,.1,.05,{"guttagonol": False, 'grimpex': False},.5)
    fp4=TDDFinalPop(numTrials,150,100,1000,.1,.05,{"guttagonol": False, 'grimpex': False},1.0)

    pylab.subplot(4, 1, 1)
    pylab.hist(fp1,bins=50)
    pylab.legend("1",loc="best")
    pylab.subplot(4, 1, 2)
    pylab.hist(fp2,bins=50)
    pylab.legend("2",loc="best")
    pylab.subplot(4, 1, 3)
    pylab.hist(fp3,bins=50)
    pylab.legend("3",loc="best")
    pylab.subplot(4, 1, 4)
    pylab.hist(fp4,bins=50)
    pylab.legend("4",loc="best")
    pylab.show()
    
    opdict["fp1"].append(fp1)
    opdict["fp2"].append(fp2)
    opdict["fp3"].append(fp3)
    opdict["fp4"].append(fp4)
    
    opdict["fp1"].append(sum(fp1)/len(fp1))
    opdict["fp2"].append(sum(fp2)/len(fp2))
    opdict["fp3"].append(sum(fp3)/len(fp3))
    opdict["fp4"].append(sum(fp4)/len(fp4))
    
    def propCured(finalPops):
        cured =0
        for popl in finalPops:
            if popl<=50:
                cured += 1
        return float(cured)/len(finalPops)
    
    opdict["fp1"].append(propCured(fp1))
    opdict["fp2"].append(propCured(fp2))
    opdict["fp3"].append(propCured(fp3))
    opdict["fp4"].append(propCured(fp4))   
    
    print "fp1: ",  opdict["fp1"][1],opdict["fp1"][2],(getMeanAndStd(fp1)[1])**2
    print "fp2: ",  opdict["fp2"][1],opdict["fp2"][2],(getMeanAndStd(fp2)[1])**2
    print "fp3: ",  opdict["fp3"][1],opdict["fp3"][2],(getMeanAndStd(fp3)[1])**2
    print "fp4: ",  opdict["fp4"][1],opdict["fp4"][2],(getMeanAndStd(fp4)[1])**2
    return opdict

op=simulationTwoDrugsDelayedTreatment(500)

def TDDFinalPop(numTrials,
                         delay,
                         numViruses=100,
                         maxPop=1000,
                         maxBirthProb=.1,
                         clearProb=.05,
                         resistances={"guttagonol": False, 'grimpex': False},
                         mutProb=.005):

    timeSteps=list(range(150+delay+150))
#    popList=[0]*len(timeSteps)
    finalPop=[0]*numTrials
    #resList=[0]*len(timeSteps)
   
    for i in range(numTrials): #in patientList:

        virusList=[]
        for j in range(numViruses):   
           virusList.append(ResistantVirus(maxBirthProb,clearProb,resistances,mutProb))
        patient=TreatedPatient(virusList,maxPop)

        for j in timeSteps[:150]:
            if patient.getTotalPop()>0:
                patient.update()
#                if resistances != {}:
#                    resList[j] += patient.getResistPop(resistances)
                
        patient.addPrescription('guttagonol')
     
        for j in timeSteps[150:150+delay]:
            if patient.getTotalPop()>0:
                patient.update()
#                if resistances != {}:
#                    resList[j] += patient.getResistPop(resistances)    
        patient.addPrescription('grimpex')
        
        for j in timeSteps[150+delay:]:
            if patient.getTotalPop()>0:
                patient.update()
                
                finalPop[i]=patient.getTotalPop()
        
    #pylab.hist(finalPop)
    #pylab.show()
    #print finalPop
    return finalPop
#    resList[:] = [float(x) / numTrials for x in resList]