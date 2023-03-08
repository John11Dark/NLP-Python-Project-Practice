#
# ? Additional NLP Exercise.

# 1. Find some text - a substantial paragraph (5 - 15 lines) and save it in a txt file.
# 2. Write a Python Program to:
# a. Read the text from file.
with open("AdditionalExercise.txt", "r") as file:
    text = file.read().lower()

# b. Clean the text (i.e. covert it to lower case and remove punctuation and digits)

# ? Challenge (2)


def expandContractions(text):
    import re

    contractionsDict = {
        "ain't": "am not",
        "aren't": "are not",
        "can't": "cannot",
        "could've": "could have",
        "couldn't": "could not",
        "didn't": "did not",
        "doesn't": "does not",
        "don't": "do not",
        "hadn't": "had not",
        "hasn't": "has not",
        "haven't": "have not",
        "he'd": "he would",
        "he'll": "he will",
        "he's": "he is",
        "i'd": "i would",
        "i'll": "i will",
        "i'm": "i am",
        "i've": "i have",
        "isn't": "is not",
        "it's": "it is",
        "it'll": "it will",
        "let's": "let us",
        "might've": "might have",
        "must've": "must have",
        "mustn't": "must not",
        "shan't": "shall not",
        "she'd": "she would",
        "she'll": "she will",
        "she's": "she is",
        "should've": "should have",
        "shouldn't": "should not",
        "that's": "that is",
        "there's": "there is",
        "they'd": "they would",
        "they'll": "they will",
        "they're": "they are",
        "they've": "they have",
        "wasn't": "was not",
        "we'd": "we would",
        "we'll": "we will",
        "we're": "we are",
        "we've": "we have",
        "weren't": "were not",
        "what'll": "what will",
        "what're": "what are",
        "what's": "what is",
        "what've": "what have",
        "where's": "where is",
        "who'll": "who will",
        "who's": "who is",
        "who've": "who have",
        "won't": "will not",
        "would've": "would have",
        "wouldn't": "would not",
        "you'd": "you would",
        "you'll": "you will",
        "you're": "you are",
        "you've": "you have",
    }

    # Compile regex pattern to match contractions
    contractionsPattern = re.compile(
        "({})".format("|".join(contractionsDict.keys())),
        flags=re.IGNORECASE | re.DOTALL,
    )

    # Define function to replace contractions with their expanded form
    def replace(match):
        contraction = match.group(0).lower()
        print("contraction: ", contraction)
        return contractionsDict.get(contraction, contraction)

    # Apply regex pattern to text and replace contractions with their expanded form
    cleanText = contractionsPattern.sub(replace, text)

    cleanText = re.sub(r"[^\w\s]", "", cleanText)  # remove punctuation
    cleanText = re.sub(r"\d", "", cleanText)  # remove digits
    return cleanText


cleanText = expandContractions(text)

# make sure that text is clean
print("clean text check: \n", cleanText)

# c. Convert the text into tokens (preferably using the nltk word_tokenizer)
from nltk.tokenize import word_tokenize

tokens = word_tokenize(cleanText)

# d. Remove stop words from the list of tokens
from nltk.corpus import stopwords

stopWords = set(stopwords.words("english"))
filtered_tokens = [token for token in tokens if token not in stopWords]

# e. Lemmatize the remaining tokens
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
lemmatizedTokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

# f. Tag the lemmatized tokens to identify nouns, verbs, adjectives, etc.
from nltk import pos_tag

taggedTokens = pos_tag(lemmatizedTokens)
# g. Output the following:

# ? Challenge (1)

#  For Point g (i) - (iv) you might have created similar code that checks for different tags.
#  Write a single function which accepts as input a list of tokens and a list of tags.
#  This function should go through the list of tokens, identify the ones that have the same
#  tags as the ones present in the list of tags supplied as input.
#  Remove any duplicate words from the remaining tokens i.e. the tokens that match the tags supplied.
#  This should avoid duplicate code by having a functor that can filter tokens based on the tags you provide.


def filterTokens(tokens, tags, tagType):
    filteredTokens = []
    for token, tag in tokens:
        if tag in tags:
            filteredTokens.append(token)
    print(tagType, "filtered tokens:", filteredTokens)
    return list(set(filteredTokens))


# i.  A list of lemmatized tokens which represent verbs.  You can group different types of verbs together e.g. verbs tagged as VB, VBD, VBG etc. can all be listed together as they are all verbs. The list outputted must contain only unique verbs i.e. no duplicates.
verbTags = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
verbs = filterTokens(
    taggedTokens,
    verbTags,
    "verbs",
)

# ii.  A list of lemmatized tokens which represent adjectives.  You can group different types of adjectives together e.g. adjectives tagged as JJ, JJR, JJS etc. can all be listed together as they are all adjectives. The list outputted must contain only unique adjectives i.e. no duplicates.
adjTags = ["JJ", "JJR", "JJS"]
adjectives = filterTokens(
    taggedTokens,
    adjTags,
    "adjectives",
)

# iii. A list of lemmatized tokens which represent common nouns.  You can group different types of common nouns together e.g. nouns tagged as NN and NPS can all be listed together as they are all common nouns. The list outputted must contain only unique common nouns i.e. no duplicates.
commonNounTags = ["NN", "NNS"]
commonNouns = filterTokens(taggedTokens, commonNounTags, "common nouns")

# iv. A list of lemmatized tokens which represent proper nouns.  You can group different types of proper nouns together e.g. nouns tagged as NNP and NNPS can all be listed together as they are all proper nouns. The list outputted must contain only unique proper nouns i.e. no duplicates
properNounTags = ["NNP", "NNPS"]
properNouns = filterTokens(taggedTokens, properNounTags, "proper nouns")

# h. Finally, generate a frequency distribution graph showing the frequency of each lemmatized token ( list created in e). Output also the 3 most frequent tokens. What do these reveal about the text? Write a comment with your observations.
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

freqDist = FreqDist(lemmatizedTokens)
freqDist.plot(30, cumulative=False)
plt.show()

mostFrequent = freqDist.most_common(3)
print("Most (3) frequent words are: ", mostFrequent)
