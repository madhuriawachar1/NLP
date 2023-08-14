import nltk

from nltk import word_tokenize, TweetTokenizer
from nltk.corpus import stopwords
from nltk.metrics.distance import edit_distance
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import words

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

def download_nltk_resources():
    try:
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        nltk.download('omw-1.4')
    except Exception as e:
        print(f"Error downloading NLTK resources: {e}")

def tokenize_text(text, tokenizer):
    return tokenizer.tokenize(text)

def remove_non_alpha_tokens(tokens):
    return [token for token in tokens if token.isalpha()]

def lowercase_tokens(tokens):
    return [token.lower() for token in tokens]

def remove_stopwords(tokens, lang):
    stop_words = set(stopwords.words(lang))
    return [token for token in tokens if token not in stop_words]

def correct_spelling(misspelled_word):
    correct_words = words.words("en")
    threshold = len(misspelled_word)
    correctly_spelled_word = ''
    
    for word in correct_words:
        if word[0] == misspelled_word[0]:
            edit_dis = edit_distance(word, misspelled_word)
            if edit_dis < threshold:
                correctly_spelled_word = word
                threshold = edit_dis
    return correctly_spelled_word

def lemmatize_word(word):
    lemmatizer = WordNetLemmatizer()
    return lemmatizer.lemmatize(word)

def stem_word(word):
    stemmer = PorterStemmer()
    return stemmer.stem(word)

if __name__ == "__main__":
    text = "I'm eating food and drinking milk."

    # Tokenization
    tokens = word_tokenize(text)
    tweet_tokenizer = TweetTokenizer()
    tweet_tokens = tweet_tokenizer.tokenize(text)

    # Cleaning Text
    alpha_tokens = remove_non_alpha_tokens(tokens)
    lowercased_tokens = lowercase_tokens(alpha_tokens)

    # Stopword Removal
    filtered_tokens = remove_stopwords(lowercased_tokens, "english")

    # Spelling Correction
    misspelled_word = "instituon"
    corrected_word = correct_spelling(misspelled_word)

    # Lemmatization
    lemmatized_word = lemmatize_word("churches")

    # Stemming
    stemmed_word = stem_word("introduction")

    print("Original Text:", text)
    print("Tokens:", tokens)
    print("Tweet Tokens:", tweet_tokens)
    print("Filtered Tokens:", filtered_tokens)
    print("Corrected Spelling:", corrected_word)
    print("Lemmatized Word:", lemmatized_word)
    print("Stemmed Word:", stemmed_word)
