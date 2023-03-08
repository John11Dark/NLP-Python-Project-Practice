import nltk

# nltk.download("stopwords")

from nltk.corpus import stopwords

print("task one")

file = open("file.txt", "r")
data = file.read()
file.close()

# print("*Data\n:", data)

tokens = data.lower().split()

# print("*tokens\n:", tokens)


# freq = nltk.FreqDist(tokens)
# for key, val in freq.items():
#     print(str(key) + ":" + str(val))


# freq.plot(20, cumulative=False)


print("task two")
print(stopwords.words("english"))

clean_tokens = tokens[:]
print("Clean tokens")
for token in tokens:
    if token in stopwords.words("english"):
        clean_tokens.remove(token)

cleanFreqTokens = nltk.FreqDist(clean_tokens)
for key, val in cleanFreqTokens.items():
    print(str(key) + ":" + str(val))


about = cleanFreqTokens.max()
print(cleanFreqTokens.most_common())

cleanFreqTokens.plot(20, cumulative=False, title="the text is about : " + about)
