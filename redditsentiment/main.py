# Entry way for the lambda
from data import get_data
from sentiment_analysis import score_data
from plot_sentiment import make_plot


def lambda_handler(x, y):
	"""
	"""
	subreddit = "funny"
	print("Building the dataframe...")
	df = get_data(subreddit)
	print("Scoring the data...")
	scores = score_data(df)
	print("Making the plot...")
	plot = make_plot(scores)
	return plot


if __name__ == "__main__":
	print(lambda_handler(None, None))
