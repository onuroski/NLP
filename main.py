from gensim import corpora
from gensim.models import LsiModel
from nltk.tokenize import RegexpTokenizer, word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from snowballstemmer import TurkishStemmer
from collections import Counter
import re
import nltk


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
    stopwords = nltk.corpus.stopwords.words('turkish')

    words = re.sub(r'[^\w\s]',"",text).split()
    return [wnl.lemmatize(word) for word in words if word not in stopwords]

#uni-gram veren fonksiyon
def unigram(text):
    unigram=nltk.ngrams(words,1)
    unigramFrequency=Counter(unigram)
    valuesOfUnigram=list(unigramFrequency.values())
    unigramlist=list(unigramFrequency)

    for x in range (0,len(unigramlist)):
        if(valuesOfUnigram[x]>0):
            print(unigramlist[x],"is used",valuesOfUnigram[x],"times")


#2-gramları veren fonksiyon
def bigram(text):
    biagrams=nltk.ngrams(words,2)
    biagramsFrequency=Counter(biagrams)
    valuesOfBiagrams=list(biagramsFrequency.values())
    biagramlist=list(biagramsFrequency)

    for x in range (0,len(biagramlist)):
        if(valuesOfBiagrams[x]>5):
            print(biagramlist[x],"is used",valuesOfBiagrams[x],"times")


# 3-gramları veren fonksiyon
def trigram(text):
    trigrams = nltk.ngrams(words, 3)
    trigramsFrequency = Counter(trigrams)
    valuesOfTrigrams = list(trigramsFrequency.values())
    triagramlist = list(trigramsFrequency)

    for x in range(0, len(triagramlist)):
        if (valuesOfTrigrams[x] > 5):
            print(triagramlist[x], "is used", valuesOfTrigrams[x], "times")


dusunce=open(r"C:\Users\ONUR\PycharmProjects\task5\tur-tr_web_2016_10K-sentences.txt", encoding="utf-8").read()
words = clean(dusunce)

unigram1 = unigram(dusunce)

bigram1 = bigram(dusunce)

trigram1 = trigram(dusunce)

print( "#"*100)
print( "#"*100)

def load_data(file_name):
    documents_list = []
    titles=[]
    with open(file_name, encoding = "utf") as fin:
        for line in fin.readlines():
            text = line.strip()
            documents_list.append(text)
    print("Total Number of Documents:",len(documents_list))
    titles.append( text[0:min(len(text),1000)] )
    return documents_list,titles


def preprocess_data(doc_set):
    # initialize regex tokenizer
    tokenizer = RegexpTokenizer(r'\w+')
    # create Turkish stop words list
    tr_stop = set(stopwords.words('turkish'))
    # Create t_stemmer of class TurkishStemmer
    t_stemmer = TurkishStemmer()
    # list for tokenized documents in loop
    texts = []
    # loop through document list
    for i in doc_set:
        # clean and tokenize document string
        raw = i.lower()
        tokens = tokenizer.tokenize(raw)
        # remove stop words from tokens
        stopped_tokens = [i for i in tokens if not i in tr_stop]
        # stem tokens
        stemmed_tokens = [t_stemmer.stemWord(i) for i in stopped_tokens]
        # add tokens to list
        texts.append(stemmed_tokens)
    return texts


def prepare_corpus(text_clean):

    # Creating the term dictionary of our courpus, where every unique term is assigned an index. dictionary = corpora.Dictionary(doc_clean)
    dictionary = corpora.Dictionary(text_clean)
    # Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in text_clean]
    # generate LDA model
    return dictionary,doc_term_matrix


def create_gensim_lsa_model(text_clean,topics,words):
    dictionary,doc_term_matrix=prepare_corpus(text_clean)
    # generate LSA model
    lsamodel = LsiModel(doc_term_matrix, num_topics=topics, id2word = dictionary)  # train model
    print(lsamodel.print_topics(num_topics=topics, num_words=words))
    return lsamodel


topics=1
words=2
doc_list,titles=load_data("tur-tr_web_2016_10K-sentences.txt")
clean_text=preprocess_data(doc_list)
model=create_gensim_lsa_model(clean_text,topics,words)