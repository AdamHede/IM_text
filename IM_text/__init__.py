from string import punctuation, digits
from ._stopwords import DANISH_STOP_WORDS, ENGLISH_STOP_WORDS
from collections import Counter
from pandas import DataFrame
from wordcloud import WordCloud
from .IM_colours import im_tricolour_a

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
