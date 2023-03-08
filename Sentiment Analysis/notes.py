from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sa = SentimentIntensityAnalyzer()
text = "A very good movie. I liked it a lot."

score = sa.polarity_scores(text)

print(score['compound'])
