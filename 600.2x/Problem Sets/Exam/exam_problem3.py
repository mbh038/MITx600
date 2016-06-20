#import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

import random
def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    global MAXRABBITPOP
    thisStepPop=CURRENTRABBITPOP
    for i in range(CURRENTRABBITPOP):
        pNewRabbit = 1.0 - thisStepPop/float(MAXRABBITPOP)
    
        if random.random()<pNewRabbit:
        #print pNewRabbit
            thisStepPop += 1
            
    CURRENTRABBITPOP=thisStepPop

            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    thisStepPop=CURRENTRABBITPOP
    thisStepFoxPop=CURRENTFOXPOP
    
    for i in range(CURRENTFOXPOP):
        
        pfer=thisStepPop/float(MAXRABBITPOP)   
        if random.random()<pfer and thisStepPop>10:
        #print "Fox eats rabbit"
            thisStepPop -=1
            if random.random() < 0.3333333:
            #print "New Fox"
                thisStepFoxPop += 1
        else:
            if random.random() < 0.1:
            #print "Fox dies"          
                if thisStepFoxPop>10:
                    thisStepFoxPop -=1
                    
    CURRENTRABBITPOP=thisStepPop
    CURRENTFOXPOP=thisStepFoxPop
    
    

            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.    """

    rabbit_populations=[]
    fox_populations = []
     
    for i in range (numSteps):
        #timeSteps.append(i)
        rabbitGrowth()
        foxGrowth()      
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
        
    return (rabbit_populations, fox_populations)


numSteps=200
rabbit_populations,fox_populations =runSimulation(numSteps)
#rabbit_populations=populations[0]
#fox_populations=populations[1]
timeSteps=range(numSteps)
pylab.figure
pylab.plot(timeSteps, rabbit_populations)
pylab.title("Rabbit populations")
pylab.legend("Rabbits",loc='best')
pylab.xlabel("Time steps")
pylab.ylabel("Population")
pylab.show()

pylab.figure
pylab.plot(timeSteps, fox_populations)
pylab.title("Fox populations")
pylab.legend("Fox",loc='best')
pylab.xlabel("Time steps")
pylab.ylabel("Population")
pylab.show()

coeff = pylab.polyfit(range(len(rabbit_populations)), rabbit_populations, 2)
pylab.figure
pylab.plot(pylab.polyval(coeff, range(len(rabbit_populations))))
pylab.show()

coeff = pylab.polyfit(range(len(fox_populations)), fox_populations, 2)
pylab.figure
pylab.plot(pylab.polyval(coeff, range(len(fox_populations))))
pylab.show()

