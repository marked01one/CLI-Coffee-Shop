from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

example_sent = '''
I don't really know
I have no idea what to order
Can you choose for me?

'''.replace("n't", " not")

quote = word_tokenize(example_sent)
lemmatized_words = [lemmatizer.lemmatize(word).lower() for word in quote]

print(lemmatized_words)


# filtered_list = []
# for word in words_in_quote:
#     if word.casefold() in stop_words and word != 'not':
#         continue
#     filtered_list.append(word.lower())

# print(filtered_list)





