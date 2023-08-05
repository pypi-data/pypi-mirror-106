from prophets import Abraham, FinvizParser
import sys, logging
from pprint import pprint
from datetime import datetime, timedelta
from finvizfinance.quote import finvizfinance

if __name__ == "__main__":
    print(f"Abraham Version: {open('version').read().strip()}")

    args = [sys.argv[1:]] if sys.argv[1:] else ["tesla"]  # default args

    # x = FinvizParser()
    # x.get_articles("tsla")

    # """
    darthvader = Abraham(
        news_source="newsapi",
        newsapi_key=open("keys/newsapi-public-2").read().strip(),
        tqdisable=False,
        bearer_token=open("keys/twitter-bearer-token").read().strip(),
    )  # splitting means that it recursively splits a large text into sentences and analyzes each individually
    print(darthvader.interest_interval
    (["btc usd", "buy bitcoin"]))
    scores = darthvader.news_sentiment(*args)  # latest date to get news from
    print("News\n--")
    pprint(scores)
    scores = darthvader.twitter_summary(
        *args,  # size=200
    )  # latest date to get news from
    print("\nTwitter\n--")
    pprint(scores)