from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


with open("reviews.txt", "r") as file:
    reviews = file.readlines()
analyzer = SentimentIntensityAnalyzer()


def getReviewsRank(reviews, analyzer):
    scoreValue = 0
    for review in reviews:
        score = analyzer.polarity_scores(review)
        print(score["compound"])
        scoreValue += score["compound"]
    return scoreValue


scoreValue = getReviewsRank(reviews, analyzer)

print("Total score: ", scoreValue)
print("Average score: ", scoreValue / len(reviews))
