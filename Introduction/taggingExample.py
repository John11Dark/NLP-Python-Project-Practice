import nltk as NLTK
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer


text = "I am going on mountains. I will climb till I can’t no more."

tokens = text.split()


for token in tokens:
    if token in stopwords.words("english"):
        tokens.remove(token)

POS_Tags = NLTK.pos_tag(tokens)


def get_part_of_speech_tags(token):
    # We are focusing on Verbs, Nouns, Adjectives and Adverbs here.
    tag_dict = {
        "J": wordnet.ADJ,
        "N": wordnet.NOUN,
        "V": wordnet.VERB,
        "R": wordnet.ADV,
    }

    tag = NLTK.pos_tag([token])[0][1][0].upper()  # eg. from [('She', 'PRP')] get P
    return tag_dict.get(tag, wordnet.NOUN)


# if no match, return Noun as the POS


lemmatizer = WordNetLemmatizer()

for token in tokens:
    lemmatisedToken = lemmatizer.lemmatize(token, get_part_of_speech_tags(token))
    print(token, lemmatisedToken)
