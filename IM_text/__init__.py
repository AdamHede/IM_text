from string import punctuation, digits
from ._stopwords import DANISH_STOP_WORDS, ENGLISH_STOP_WORDS

digits_and_punctuation = punctuation + digits

def clean_string(text, lower_case = True, remove='digits and punctuation', stopwords='danish'):
    if lower_case:
        text = text.lower()
    if remove == 'digits and punctuation':
        remove = digits_and_punctuation
    if remove is not None:
        text = text.translate(str.maketrans(remove, " " * len(remove)))
    if stopwords is not None:
        if stopwords is 'danish':
            stopwords = DANISH_STOP_WORDS
        elif stopwords is 'english':
            stopwords = ENGLISH_STOP_WORDS
        else:
            stopwords = stopwords
        text = [word for word in text.split() if word not in stopwords]
        text = " ".join(text)
    return text