#Third Party Module

#STOPWORD REMOVER

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')
nltk.download('stopwords')
stop_words=set(stopwords.words("english"))
text= " This is sample sentence and my name Atharv"
words=word_tokenize(text)
filtered_words = [word for word in words if word.lower() not in stop_words]
print(filtered_words)