## Week 1
def lotsOfParameters1(a,b,c,d,e):
    print a
    print b
    print c
    print d
    print e

def lotsOfParameters2(a=1,b=2,c=3,d=4,e=5):
    print a
    print b
    print c
    print d
    print e

def lotsOfParameters3(a,b,c=3,d=4,e=5):
    print a
    print b
    print c
    print d
    print e
    
import pylab
def loadFile():
    inFile = open('julyTemps.txt')
    day=[]
    high=[]
    low=[]
    for line in inFile:
        fields=line.split()
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low,high)
            
        
def producePlot(lowTemps, highTemps):
    diffTemps=[]
    for i in range(len(lowTemps)):
        diffTemps.append(highTemps[i]-lowTemps[i])
    
    pylab.plot(range(1,32), diffTemps)
    pylab.title("Day by Day Ranges in Temperature in Boston in July 2012")
    pylab.xlabel('Days')
    pylab.ylabel("Temperature Ranges")
    pylab.show()
    pylab.savefig('Temperature range plot') #save figure 1


(low,high)=loadFile()
print len(low)
producePlot(low,high)