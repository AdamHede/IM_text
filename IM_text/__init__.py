from string import punctuation, digits

digits_and_punctuation = punctuation + digits

with open("IM_text/stopwords_da.txt", "r") as file:
    stopwords_da = file.read().splitlines()

with open("IM_text/stopwords_en.txt", "r") as file:
    stopwords_en = file.read().splitlines()

def clean_string(text, lower_case = True, remove='digits and punctuation', stopwords='danish'):
    if lower_case:
        text = text.lower()
    if remove is 'digits and punctuation':
        remove = digits_and_punctuation
    if remove is not None:
        txt = text.translate(str.maketrans(remove, " " * len(remove)))
    if stopwords is 'danish':
        txt = [word for word in txt.split() if word not in stopwords_da]
        txt = " ".join(txt)
    elif stopwords is "english":
        txt = [word for word in txt.split() if word not in stopwords_en]
        txt = " ".join(txt)
    return txt