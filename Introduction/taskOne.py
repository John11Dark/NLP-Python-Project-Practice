from nltk import sent_tokenize,word_tokenize, wordpunct_tokenize

input = "Let's go to Beijing!"

print (input)
print ("Whitespace tokenisation", input.split())

print ("Word tokenisation",word_tokenize(input))

print ("Punctuation tokenisation",wordpunct_tokenize(input))

print ("Sentence tokenisation",sent_tokenize(input))
