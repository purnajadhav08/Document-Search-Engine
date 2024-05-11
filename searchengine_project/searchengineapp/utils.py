import re
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

def preprocess_text(text, document_id):
    # Remove special characters and convert to lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    
    # Tokenize the text
    tokens = word_tokenize(text)

    # Initialize Porter Stemmer
    stemmer = PorterStemmer()

    # Apply stemming to tokens
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    # Create positional index
    positional_index = {}
    for i, token in enumerate(stemmed_tokens):
        if token not in positional_index:
            positional_index[token] = {}
        if str(document_id) not in positional_index[token]:
            positional_index[token][str(document_id)] = [i]
        else:
            positional_index[token][str(document_id)].append(i)

    return positional_index
