import matplotlib.pyplot as plt
import pandas as pd

def make_plot(df):
    df = df["compound"].rolling(400).mean()
    plt.plot(df)
    plt.xlabel("Comment Number")
    plt.ylabel("Compound Sentiment Score")
    plt.title("Running mean of Compound sentiment score of posts, r All, top Day, 50 posts.")
    plt.show()
