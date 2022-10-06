from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.lancaster import LancasterStemmer
from config import FLAVOUR_CHECK

class NLP:
    def __init__(self, input_sentence) -> None:
        self.input = input_sentence.replace("n't", " not").replace(" not", " no")
        self.stemmed_quote = self._stemmer(self.input)
        print(self.stemmed_quote)
        pass
    
    def _stemmer(self, token_quote):
        """Return a list of all words from the input sentence returned to their original meaning
        
        Example:
            diversification, diversity --> diverse
            differentiate, differentials --> difference

        Args:
            token_quote (str): 

        Returns:
            List: a list of words from the input with their root meaning
        """
        quote_list = word_tokenize(token_quote)
        lemmatizer = WordNetLemmatizer()
        stemmer = LancasterStemmer()
        
        lmtz_list = [lemmatizer.lemmatize(word) for word in quote_list]
        return [stemmer.stem(word) for word in lmtz_list]

input_sent = input("What order do you want today?\n")
processor = NLP(input_sent)

