#zeyrek paketlerini indirdim
import nltk
from nltk import pos_tag

txt = open(r"C:/Users/ONUR/PycharmProjects/pythonProject1/asikveysel.txt",encoding="utf-8").read()
tokens = nltk.word_tokenize(txt)
tag = pos_tag(tokens)

for i in tag:
    print(i)

print("###"*50)

import zeyrek
pos = zeyrek.MorphAnalyzer()
txt = open(r"C:/Users/ONUR/PycharmProjects/pythonProject1/asikveysel.txt",encoding="utf-8").read()
postags=pos.analyze(txt)

for i in postags:
    try:
        print(i[0].word,i[0].pos)
    except:
        pass