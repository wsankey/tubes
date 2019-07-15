# Perform sentiment analysis
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_analyser_score(df):
    analyser = SentimentIntensityAnalyzer()

    df_sentiment = pd.DataFrame(columns=["neg","neu","pos","compound"])
    values = list(df.values.flatten())
    for row in values:
        score = analyser.polarity_scores(row)
        print(score)
        df_sentiment = df_sentiment.append({"neg":score["neg"],"neu":score["neu"],"pos":score["pos"],"compound":score["compound"]},
                                           ignore_index=True)
    return df_sentiment


def score_data(df):
    """
    """
    _df = sentiment_analyser_score(df)
    return _df
