# Problem Set 1
# Problem 2
# Counting Bobs

s=raw_input("Enter a string:")
print s

nbob=0

for i in range(0,len(s)-2):
    if s[i]=="b":
        if s[i+1]=="o":
            if s[i+2]=="b":
                nbob += 1
            
print ("Number of times bob occurs is: "+str(nbob))
