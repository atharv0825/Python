#tokenization 

import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
nltk.download('punkt')
text = "this is the sample sentence used for the test"
words = word_tokenize(text)
print(words)
sentence = sent_tokenize(text)
print(sentence)<|eom_id|><|start_header_id|>assistant<|end_header_id|>