import difflib

s1='nasılsınız'
s2='nasılsnz'
print(difflib.SequenceMatcher(None,s1,s2,False).ratio())

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

s1="Doğal dil işleme, yapay zekanın bir alt kategorisidir."
s2="İngilizce Almanca Fransızca ve İspanyolca en sık kullanılan dil kategorisimdedir."
print("Fuzzywuzzy Ratio", fuzz.ratio(s1,s2))

query ='aynı'
choices = ['ayna', 'aydan', 'aytaç', 'balayı', 'alay']
print("List of ratios")
print(process.extract(query,choices), '\n')
print("Best anang the above list:", process.extractOne(query,choices))

import nltk
import re
from collections import Counter
nltk.download('stopwords')
import difflib


def basic_clean(text):
    wnl = nltk.stem.WordNetLemmatizer()
    stopwords= nltk.corpus.stopwords.words('turkish')
    words = re.sub(r'[^\w\s]', '', text).split()
    return [wnl.lemmatize(word) for word in words if word not in stopwords]

open_file=open('tasktext.txt', encoding="utf-8")
df=open_file.read()
words=basic_clean(df)

low=nltk.ngrams(words,1)
lowFrequency = Counter(low)
valuesOfLowFrequency=list(lowFrequency.values())
lowFrequencyList = list(lowFrequency)

for x in range(0, len(lowFrequencyList)):
    if(valuesOfLowFrequency[x]<5):
        print(lowFrequencyList[x], "is used", valuesOfLowFrequency[x],"times")


print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

high=nltk.ngrams(words,1)
highFrequency = Counter(high)
valuesOfHighFrequency=list(highFrequency.values())
highFrequencyList = list(highFrequency)

for x in range(0, len(highFrequencyList)):
    if(valuesOfHighFrequency[x]>5):
        print(highFrequencyList[x], "is used", valuesOfHighFrequency[x],"times")


low_freq_list="""elam armtu"""
low_freq_list=low_freq_list.split()

high_freq_list="""elma armut"""
high_freq_list=high_freq_list.split()

for token1 in low_freq_list:
    for token2 in high_freq_list:
        mylist=[(token1.splitlines(),token2.splitlines()), "Similarity=>", difflib.SequenceMatcher(None,token1,token2,False).ratio()]
        print(mylist)

"""mylist2=[(token1.splitlines(),token2.splitlines()),difflib.SequenceMatcher(None,token1,token2,False).ratio()]"""

print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

for token1 in high_freq_list:
    for token2 in low_freq_list:
        mylist2=[(token1.splitlines(),token2.splitlines()), "Similarity=>", difflib.SequenceMatcher(None,token1,token2,False).ratio()]
        print(mylist2)
