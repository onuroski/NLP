import nltk
from collections import Counter
import re

#POS-Tag yapması için bir fonksiyon yazıyorum...
def tagging(sent):

    lower_case=sent.lower()
    tokens=nltk.word_tokenize(lower_case)
    tags=nltk.pos_tag(tokens)           #pos taglerine ayırıyorum, ögelerine ayırmak anlamına geliyor
    counts=Counter(tag for word,tag in tags)        #pos tagleri saymak için sayaç
    print (counts)

#stopwordsleri ayıklayan fonksiyon
def clean(text):
    wnl=nltk.stem.WordNetLemmatizer()
    stopwords = nltk.corpus.stopwords.words('english')

    words = re.sub(r'[^\w\s]',"",text).split()
    return [wnl.lemmatize(word) for word in words if word not in stopwords]

#uni-gram veren fonksiyon
def unigram(text):
    unigram=nltk.ngrams(words,1)
    unigramFrequency=Counter(unigram)
    valuesOfUnigram=list(unigramFrequency.values())
    unigramlist=list(unigramFrequency)

    for x in range (0,len(unigramlist)):
        if(valuesOfUnigram[x]>2):
            print(unigramlist[x],"is used",valuesOfUnigram[x],"times")


#2-gramları veren fonksiyon
def bigram(text):
    biagrams=nltk.ngrams(words,2)
    biagramsFrequency=Counter(biagrams)
    valuesOfBiagrams=list(biagramsFrequency.values())
    biagramlist=list(biagramsFrequency)

    for x in range (0,len(biagramlist)):
        if(valuesOfBiagrams[x]>1):
            print(biagramlist[x],"is used",valuesOfBiagrams[x],"times")


# 3-gramları veren fonksiyon
def trigram(text):
    trigrams = nltk.ngrams(words, 3)
    trigramsFrequency = Counter(trigrams)
    valuesOfTrigrams = list(trigramsFrequency.values())
    triagramlist = list(trigramsFrequency)

    for x in range(0, len(triagramlist)):
        if (valuesOfTrigrams[x] > 1):
            print(triagramlist[x], "is used", valuesOfTrigrams[x], "times")


f=open(r"D:\o\task3.txt","r")
coffee =f.read()
words = clean(coffee)

unigram1 = unigram(coffee)

bigram1 = bigram(coffee)

trigram1 = trigram(coffee)

print( "#"*100)
POStag = tagging(coffee)
print( "#"*100)

f=open(r"D:\o\task3_2.txt","r")
covid =f.read()

words =clean(covid)

unigram2 =unigram(covid)
bigram2 =bigram(covid)
trigram2 = trigram(covid)
POStag2 =tagging(covid)