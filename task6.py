
from snowballstemmer import TurkishStemmer

turkStem = TurkishStemmer()
from nltk.tokenize import word_tokenize

dict_cay = {1: "yeryüzünün denizlerle kaplı olmayan bölümü, yer, toprak", 2: "En koyu renk, siyah, ak, beyaz karşıtı"}
sentences = ['küçük topraklar kara parçası gibi göründü', 'kara gözleri adeta bir renk gibi içime işliyordu']


def by_value(item):
    return item[1]


def lesk(sentence, dict_s, word):
    y = {}
    z = 0

    sentence = word_tokenize(sentence)
    for i in range(len(sentence)):
        sentence[i] = turkStem.stemWord(sentence[i])

    for key, value in dict_s.items():
        x = 0
        k = word_tokenize(value)

        for i in range(len(k)):
            k[i] = turkStem.stemWord(k[i])

            for j in range(len(sentence)):
                if sentence[j] == k[i]:
                    x += 1

        y[key] = x

    for k, v in sorted(y.items(), key=by_value):
        z = k

    return dict_s[z]


p = lesk(sentences[1], dict_cay, "kara")

print(p)
