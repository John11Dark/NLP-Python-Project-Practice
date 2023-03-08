import nltk

# nltk.download()

from nltk.tokenize import word_tokenize, sent_tokenize, wordpunct_tokenize

# Open file containing text input
file = open("file.txt", "r")
fileContent = file.read()
file.close()

# Display file content i.e. raw text
print(fileContent)

# Tokenize  using white spaces
whitespace_tokens = fileContent.lower().split()
print(whitespace_tokens)

# Calculate the frequency distribution of each of the white space tokens
whitespace_tokens_freq = nltk.FreqDist(whitespace_tokens)

# Display the frequency of each of the white space tokens
for key, val in whitespace_tokens_freq.items():
    print(str(key) + ":" + str(val))

# Create a graph based on the frequencies of each white space token
whitespace_tokens_freq.plot(20, cumulative=False)

# Tokenize using word tokenizer
word_tokens = word_tokenize(fileContent)

# Calculate the frequency distribution of each of the word tokens
word_tokens_freq = nltk.FreqDist(word_tokens)

# Display the frequency of each of the word tokens
for key, val in word_tokens_freq.items():
    print(str(key) + ":" + str(val))

# Create a graph based on the frequencies of each word token
word_tokens_freq.plot(20, cumulative=False)
