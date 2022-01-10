# task7 First, low and high frequency words (for threshold = 5) should be determined in a Turkish collection. Words with low frequency will be assumed to have spelling errors. To solve this problem, a Lexical Similarity function will be used (student can find at internet or prepare) and it will be suggested that these erroneous assumed words can change to the most lexically similar word from high-frequency words. The code to be prepared must give a two-column list: low-frequency words in the first column and the most lexically similar high-frequency words in the second column.



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
