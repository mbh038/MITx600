# Problem Set 1
# Problem 1
# Counting Vowels

s=raw_input("Enter a string:")
print s

numVowels=0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
print 'Number of vowels: ' + str(numVowels) 
