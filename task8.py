import spacy
import pandas as pd
import numpy as np
from spacy.vectors import Vectors
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
nlp = spacy.load('en_core_web_lg')
df = open(r"C:\Users\ONUR\Downloads\Documents\eng_news_2008_10K\500sentences.txt", encoding="utf-8").read()
print(df[2])
print(df.head())
print(df.shape)
df.head()
print(df.head)
sentence_vector = [nlp(x).vector for x in df['text'].values]
sentence_vector = np.stack(sentence_vector, axis=0 )
print(sentence_vector.shape)
svd = TruncatedSVD(n_components=10)
svd_sentences = svd.fit_transform(sentence_vector)
print(svd_sentences)
cos_sim=cosine_similarity(svd_sentences, svd_sentences)
degisken=pd.DataFrame(cos_sim)[18].sort_values(ascending=False)[:10]
print("data frame")
print(degisken)
print("değisken\n")
print(df['text'][18],'\n')
print(df['text'][28],'\n')
my_sentece_vec = np.stack([nlp("It's a chill and calm game").vector])
sentence_vector=np.append(sentence_vector,my_sentece_vec,axis=0)
print(sentence_vector.shape)
svd_sentences = svd.fit_transform(sentence_vector)
cos_sin=cosine_similarity(svd_sentences,svd_sentences)
degisken2=pd.DataFrame(cos_sin)[107].sort_values(ascending=False) [:10]
print("DEGISKEN2 DEGERİ")
print(degisken2,'\n')
print("It's a chill and calm game", '\n')
print(df['text'][46])