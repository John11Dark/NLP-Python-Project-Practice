# 1.	Read the contents of the text files into an array of string, where each textfile will occupy one location of the array


filesArray = []

with open("music.txt", "r") as file:
    filesArray.append(file.read().replace("\n", " "))

with open("sport.txt", "r") as file:
    filesArray.append(file.read().replace("\n", " "))

with open("animals.txt", "r") as file:
    filesArray.append(file.read().replace("\n", " "))

with open("earthquakes.txt", "r") as file:
    filesArray.append(file.read().replace("\n", " "))

with open("weather.txt", "r") as file:
    filesArray.append(file.read().replace("\n", " "))


# 2.	Create a TfidfVectorizer, removing the stop words at the same time, as follows:

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words="english")


# 3.	Generate the TFIDF matrix using the array of strings and vectoriser

tfidf_matrix = vectorizer.fit_transform(filesArray)
# 4.	For each textfile, print the most important token in that file, i.e. the token with the highest TFIDF value


for i in range(0, len(filesArray)):
    # Get the TFIDF values for the current file

    tfidf_values = tfidf_matrix.toarray()[i]  # type: ignore

    # Get the feature names
    feature_names = vectorizer.get_feature_names_out()

    # Get the index of the highest TFIDF value

    max_index = tfidf_values.argmax()

    # Get the token with the highest TFIDF value

    max_token = feature_names[max_index]
    print("File: ", i)
    print("Most important token: ", max_token)
    print("TFIDF value: ", tfidf_values[max_index])
    # print("File content: ", filesArray[i], "==================================\n\n")
    print("==================================\n")

    # compare the five files and find the most similar pair of files

from sklearn.metrics.pairwise import cosine_similarity

for i in range(0, len(filesArray)):
    for j in range(i + 1, len(filesArray)):
        similarity = cosine_similarity(tfidf_matrix[i], tfidf_matrix[j])
        print("File: ", i, " and File: ", j)
        print("Cosine similarity: ", similarity[0][0])
        print("==================================\n")
