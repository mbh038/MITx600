# Problem Set 1
# Problem 3
# Alphabetical Substrings

s=raw_input("Enter a string:")
s=s.lower()
print s

lastchar="a"
temp=[]
subs=[]
for char in s:
    #print char
    if char >= lastchar:
        temp.append(char)
        #print temp
    else:
        subs.append("".join(temp))
        temp=[]
        temp.append(char)
        
    lastchar=char
subs.append("".join(temp))
# print len(subs),subs

longest = 0
index=0
for i in range(0,len(subs)):
    if i == len(subs):
        break
    if len(subs[i])>longest:
        longest=len(subs[i])
        index=i
          
#print index,longest

print ("Longest substring in alphabetical order is: "+str(subs[index]))
