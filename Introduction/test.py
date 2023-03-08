import nltk

# nltk.download("punkt")

from nltk.tokenize import word_tokenize


fileContent = "Hello there world!"

tokenized_word = word_tokenize(fileContent)

print(tokenized_word)
