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
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            print(post.get("data").get("title"))
    else:
        print("None")


if __name__ == "__main__":
    subreddit = argv[1]
    top_ten(subreddit)
