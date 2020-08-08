import textract
import nltk
import re
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
nltk.download("stopwords")


def find_keywords(filename):
    in_string = textract.process(filename)
    in_string = str(in_string, "utf-8")
    temp = re.sub("[^a-zA-Z]", " ", in_string)
    temp = temp.lower()
    temp = temp.split()
    english_stopwords = stopwords.words("english")
    porter_stemmer = PorterStemmer()
    out = []
    for word in temp:
        if word not in set(english_stopwords) and len(word) > 2:
            out.append(porter_stemmer.stem(word))
    return list(dict.fromkeys(out))

