import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets.loc[tweets["content"].str.len() > 15][["tweet_id"]]


if __name__ == "__main__":
    data = [[1, 'Let us Code'], [2, 'More than fifteen chars are here!']]
    tweets_test = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id': 'Int64', 'content': 'object'})

    print(invalid_tweets(tweets_test))