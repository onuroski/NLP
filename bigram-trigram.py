# Creating bigrams and trigrams
#Using N-gram analysis, list all 2-grams and 3-grams according to a certain threshold (eg, more than 5 in frequency) in a Turkish corpus. With these study, emphasize the importance of lematization for Turkish. Also, comment on what purpose this application can be used in the real world.

import nltk


nltk.download('stopwords') # anlam ifade etmeyen kelimeleri "acaba,bu,ne,kim" ayıklamak için
from collections import Counter #gram ve trigramların kaç sefer geçtiğini saymak için

import re

f = open(r"D:\o\onur.txt", "r", encoding="utf-8")
text = f.read()
from nltk.corpus import stopwords

my_stopwords = set(stopwords.words('turkish')) #stopwordlerin türkçe olanlarını ayıklamak için
words = []
words = re.sub(r'[^\w\s]', "", text).split()

# Tokenization using word_tokenize()
all_tokens = nltk.word_tokenize(text)

for token in all_tokens:            #stopwords değilse ekleme yapmasını eklemesini sağlıyoruz
    if token not in my_stopwords:
        words.append(token)

" ".join(words)             #stopwords ise if bloğundan ayrılıp boşuk yazdırıyoruz


biagrams = nltk.ngrams(words, 2)
biagramsFrequency = Counter(biagrams)
valuesOfBiagrams = list(biagramsFrequency.values())
biagramlist = list(biagramsFrequency)

for x in range(0, len(biagramlist)):
    if (valuesOfBiagrams[x] > 5):
        print(biagramlist[x], "is used", valuesOfBiagrams[x], "times")

trigrams = nltk.ngrams(words, 3)
trigramsFrequency = Counter(trigrams)
valuesOfTrigrams = list(trigramsFrequency.values())
triagramlist = list(trigramsFrequency)

for x in range(0, len(triagramlist)):
    if (valuesOfTrigrams[x] > 5):
        print(triagramlist[x], "is used", valuesOfTrigrams[x], "times")
