# Grab Reddit data
import config
import praw
import pandas as pd


def initialize_reddit_app():
    """
    """
    client_id = config.CLIENT_ID
    client_secret = config.CLIENT_SECRET
    user_agent = config.USER_AGENT

    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent,
                         )
    return reddit


def get_posts(reddit, subreddit):
    """
    """
    posts = []
    hot_posts = reddit.subreddit(subreddit).top('day', limit=10)
    
    for post in hot_posts:
        posts.append(post.id)

    return posts


def get_comments(reddit, posts_id):
    """
    """
    df_comments = pd.DataFrame()

    for _id in posts_id:
        submission = reddit.submission(id=_id)
        submission.comments.replace_more(limit=None)

        for comment in submission.comments.list():
            try:
                df_comments = df_comments.append([comment.body], ignore_index=True)
            except AttributeError:
                pass

    return df_comments


def get_data(subreddit):
    """
    Return a dataframe of comments for subreddit
    """
    reddit = initialize_reddit_app()
    postids = get_posts(reddit, subreddit)
    df = get_comments(reddit, postids)
    return df
