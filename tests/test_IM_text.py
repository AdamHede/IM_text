from IM_text import clean_string, count_words, create_wordcloud, topic_model
from .CONST import HAVET_ER_SKØNT

text = "Havet er skønt, Havet er skønt, Ingen bliver slået, Renset og flået!"

def test_clean_string():
    expected_out = "havet skønt havet skønt slået renset flået"
    out = clean_string(text)
    assert expected_out == out, "Default functions of clean_string failed to reproduce correct response"

def test_count_words():
    out = count_words(text)
    assert out.loc[0, 'word'] == "Havet"
    assert out.loc[8, 'word'] == "flået!"
    assert out.loc[0, 'count'] == 2
    assert out.loc[8, 'count'] == 1

def test_create_wordcloud():
    try:
        out = create_wordcloud(text)
    except Exception:
        assert False, "create_wordcloud somehow failed. Sorry to not be more specific, this is still under development."

def test_topic_model():
    try:
        topic_dict, topics, vectorizer, model = topic_model(HAVET_ER_SKØNT, n_topics=4)
    except Exception:
        assert False, "Topic model somehow failed. Sorry to not be more specific, this is still under development."