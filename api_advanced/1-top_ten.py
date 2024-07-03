#!/usr/bin/python3
"""
Python script that returns the number of top hot posts
    for a given subreddit
"""
import requests
from sys import argv


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{subreddit}/hot.json?limit=10".format(
        subreddit=subreddit
    )
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
    else:
        print("None")
        return


if __name__ == "__main__":
    subreddit = argv[1]
    if len(argv) < 2:
        print("Please pass an argument")
    else:
        top_ten(subreddit)
