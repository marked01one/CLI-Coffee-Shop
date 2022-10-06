from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.lancaster import LancasterStemmer


lemmatizer = WordNetLemmatizer()
stemmer = LancasterStemmer()

example_sent = '''
diversification, diverse, diversify, diversity
'''

quote = word_tokenize(example_sent)
lemmatized_words = [lemmatizer.lemmatize(word).lower() for word in quote]
stemmed_words = [stemmer.stem(word).lower() for word in quote]

print(lemmatized_words)
print([lemmatizer.lemmatize(word) for word in stemmed_words])


# filtered_list = []
# for word in words_in_quote:
#     if word.casefold() in stop_words and word != 'not':
#         continue
#     filtered_list.append(word.lower())

# print(filtered_list)





