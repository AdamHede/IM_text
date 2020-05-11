from string import punctuation, digits
from ._stopwords import DANISH_STOP_WORDS, ENGLISH_STOP_WORDS
from collections import Counter
from pandas import DataFrame
from wordcloud import WordCloud
from .IM_colours import im_tricolour_a
from .utils import _display_topics
import inspect
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from afinn import Afinn
from numpy import tanh

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation, TruncatedSVD

digits_and_punctuation = punctuation + digits


def clean_string(text, lower_case = True, remove='digits and punctuation', stopwords='danish'):
    """
    A simple function which cleans a string, using sensible default settings.
    :param text: A text string.
    :param lower_case: Convert all characters lowercase
    :param remove: a string of characters and symbols to remove. Default is punctuation and digits found in strings
    :param stopwords: A list, set or frozenset of stopwords to not include. Can also be "danish" or "english" for built
    built in lists. Default is danish (a pretty aggressive list).
    :return: a cleaned string
    """
    if lower_case:
        text = text.lower()
    if remove == 'digits and punctuation':
        remove = digits_and_punctuation
    if remove is not None:
        text = text.translate(str.maketrans(remove, " " * len(remove)))
    if stopwords is not None:
        if stopwords.lower() == 'danish':
            stopwords = DANISH_STOP_WORDS
        elif stopwords.lower() == 'english':
            stopwords = ENGLISH_STOP_WORDS
        else:
            stopwords = stopwords
        text = [word for word in text.split() if word not in stopwords]
        text = " ".join(text)
    return text

def count_words(text, format='dataframe'):
    """
    Counts words in a string, returning either a Counter-object or a dataframe
    :param text: A text string (ofte a union of multiple strings)
    :param format: if 'datarame' returns a pandas dataframe. If 'counter', returns a collections.counter object.
    default is 'dataframe'
    :return: DataFrame or Counter.
    """
    c = Counter(text.split())
    if format.lower() == "dataframe":
        out = DataFrame(c.most_common(), columns=['word', 'count'])
    elif format.lower() == "counter":
        out = c
    else:
        raise Exception("Format must be one of dataframe or counter")
    return out


def create_wordcloud(text, width=1920, height=1080, font_path="Arial.ttf", background_color='white',
                     colormap="Implement", collocations=False, max_words=200, relative_scaling='auto',
                     to_file=None):
    """
    A simple function to quickly produce a wordcloud in implement-style. optionally saves the renderded
    :param text: A collection of text in a single string
    :param width: Width of the final output. Default = 1920
    :param height: Height of the final output. Default = 1080
    :param font_path: Path to a font to use. Default is included "Arial.ttf"
    :param background_color: Background color of the final image. Default is white.
    :param colormap: Colormap to use. Can be matplotlib LinearSegmentedColormap. See IM_colours from multiple options.
    Default is "Implement", automatically loads tri-colour Implement-style.
    :param collocations: Determines if common bigrams (i.e. two words commonly occouring together) gets their own position.
    Default is "False"
    :param max_words: Maximum number of words to display. Default is 200
    :param relative_scaling: Relative scaling of the words. 0=Only word rank is considered,
    1=Relative occourance of word is fully considered. Default is "auto", which is equals to 0.5.
    :param to_file: A string to save the file to. If none provided, just returns the wordcloud object. Default is None.
    :return: Wordcloud object.
    """
    print(f"Creating wordcloud")
    text = [word.capitalize() for word in text.split()]
    text = " ".join(text)
    if colormap == "Implement":
        colormap = im_tricolour_a
    wc = WordCloud(width=width,
                   height=height,
                   font_path=font_path,
                   background_color=background_color,
                   colormap=colormap,
                   collocations=collocations,
                   max_words=max_words,
                   relative_scaling=relative_scaling).generate(text)
    if isinstance(to_file, str):
        wc.to_file(to_file)
    return wc

def topic_model(texts, n_topics=20, words_to_display=20, vectorizer='tfidf', ngram_range=(1,1), max_df=0.95, min_df=3, max_features=1000,
                method='NMF'):
    """
    A function to quickly perform basic topic modelling tasks.
    :param texts: A series of text documents.
    :param n_topics: Number of topics to attempt to identify. Default is 20.
    :param n_words: Number if words to display when topics are found. Default is 20.
    :param vectorizer: A sklearn style vectorizer. Either CountVectorizer or TfidfVectorizer. Default is "tfidf" which identifies a good default vectorizer.
    :param ngram_range: Tuple. Only used with the default vectorizer. The range of n-grams to vectorizer. Default is (1,1)
    :param max_df: Int or Float. Only used with the default vectorizer. Maximum number of occourances of a word. Default is 95% of documents.
    :param min_df: Int or float. Only used with the default vectorizer. Minimum number of occournaces if a word. Default is 3.
    :param max_features: Int. Only used with the default vectorizer. Maximum number of words to use. Default is 1000
    :param method: Must be a sklearn decomposition class, either NMF, LDA or SVD or a string with one of the acronyms to use a default method. Default is "NMF",
    :return: topic_dict = A dictionary with topic numbers and most common words.
    topics = A matrix of size (documents x topics) providing loadings for each topic
    vectorizer = The fitted vectorizer
    model = The fitted model based on the chosen method.
    """
    if vectorizer == 'tfidf':
        vectorizer = TfidfVectorizer(ngram_range=ngram_range, max_df=max_df, min_df=min_df, max_features=max_features)
    elif inspect.isclass(vectorizer):
        vectorizer = vectorizer
    else:
        raise Exception("Vectorizer must be a sklearn-style vectorizer")
    matrix = vectorizer.fit_transform(texts)
    feature_names = vectorizer.get_feature_names()

    if method.lower() == "nmf":
        model = NMF(n_components=n_topics)
    elif method.lower() == "lda" or method.lower == "latentdirichletallocation":
        model = LatentDirichletAllocation(n_components=n_topics, n_jobs=-1)
    elif method.lower() == "svd" or method.lower() == 'truncatedsvd':
        model = TruncatedSVD(n_components=n_topics)
    elif inspect.isclass(method):
        model = method
    else:
        raise Exception("Method must be either NMF, LDA, SVD or a costum version of one of these.")
    topics = model.fit_transform(matrix)

    topic_dict = {}
    topic_list = []
    for topic_idx, topic in enumerate(model.components_):
        print(f"Topic {topic_idx}:")
        topic_dict[topic_idx] = [feature_names[i] for i in topic.argsort()[:-words_to_display - 1:-1]]
        topic_list.append("_".join([feature_names[i] for i in topic.argsort()[:-3 - 1:-1]]))
        print(" ".join(topic_dict[topic_idx]))
    topics = DataFrame(topics, columns=topic_list)

    return topic_dict, topics, vectorizer, model


def extract_bert_vectors(texts, per_token=True):
    """
    This module uses Easy Bert. Read more at: https://github.com/robrua/easy-bert
    Defaults to use Google's official most recent (as of May 8. 2020) multilingual model: bert_cased_L-24_H-1024_A-16
    https://tfhub.dev/google/bert_cased_L-24_H-1024_A-16/1

    Also available is a danish fine-tuned version. Go to: https://github.com/botxo/nordic_bert
    Download a recent version, unzip it and point EasyBert to it's location.

    Similar methods can be followed for common Bert alternatives as well as task-specifically fine-tuned models

    WARNING: I can't get that to work right now...
    :param texts:
    :return:
    """
    try:
        from easybert import Bert
    except ImportError:
        print("Please install easybert. Notice, this might downgrade your TensorFlow installation to 1.x")
    bert_url = "https://tfhub.dev/google/bert_multi_cased_L-12_H-768_A-12/1"
    print(f"Downloading BERT model from: {bert_url}")
    bert = Bert(bert_url)
    print("Download done, now extracting vectors")
    with bert:
        out = bert.embed(texts, per_token=per_token)
    return out


def afinn_wrapper(text):
    afinn = Afinn(language="da", emoticons=True)
    return tanh(afinn.score(text))

def vader_wrapper(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    return scores['compound']

def sentiment_analysis(text, lang='da'):
    """
    Basic sentiment analysis function. Works with either danish through Afinn or english through Vadar
    Note the danish implementation (Afinn) is unbounded, and therefore pushed through a tanh-transformation.
    It makes it often go towards extreme values.
    :param text: A text string
    :param lang: Language to do sentiment analysis for. da (Danish) or en (English). Default is Danish.
    :return: A sentiment score between -1 (negative) and 1 (positive).
    """
    if lang.lower()[:2] == 'da':
        return afinn_wrapper(text)
    elif lang.lower()[:2] == 'en':
        return vader_wrapper(text)
    else:
        raise Exception("Language must be either da (danish) or en (english)")