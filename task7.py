#pip install fuzzywuzzy
#pip install python-Levenshtein

import nltk
from fuzzywuzzy import process


data = open(r"C:\Users\ONUR\PycharmProjects\task7_2\tasktext.txt", encoding="utf-8")
raw=data.read()
token=nltk.word_tokenize(raw) #tokenization
wordFrequence=nltk.FreqDist(token) #frequence of the words

i=0
high=[]
low=[]

for a, l in wordFrequence.items():
    if len(a)>1:
        if 5<l and i<150:
            i+=1
            print(a,l)
            high.append(a)
        if 5>l and i<150:
            i+=1
            print(a,l)
            low.append(a)
print("\n \n ")

print("Low Frequence:      |       High Frequence")
for word in low:
    value = process.extract(word,high)
    similarWord=value[0][0]
    similarity=value[0][1]
    print(word,":     ->       ",similarWord, "\n")