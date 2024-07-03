#!/usr/bin/python3
"""
Python script that returns the number of subscribers
    for a given subreddit
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "custom-script/1.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json().get("data", {}).get("subscribers", 0)
    except requests.RequestException:
        return 0
    return 0


if __name__ == "__main__":
    if len(argv) > 1:
        subreddit = argv[1]
        print(number_of_subscribers(subreddit))
    else:
        print("No subreddit provided")
