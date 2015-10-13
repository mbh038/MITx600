import string
word="$%^Hello World!"
for i in range(len(string.punctuation)):
    word=word.replace(string.punctuation[i],"")
word=word.lower()
word=word.split(" ")
print word[0],word[1]

def isWordIn(self,text):
    for i in range(len(string.punctuation)):
        text=text.replace(string.punctuation[i],"")
        text=text.lower()
        text=text.split(" ")
    return word in text
