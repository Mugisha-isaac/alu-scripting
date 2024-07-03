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
    url = "https://www.reddit.com/r/{subreddit}/about.json".format(subreddit=subreddit)
    headers = {"User-Agent": "custom-script/1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json().get("data", {}).get("subscribers", 0)
        elif response.status_code == 404 or response.status_code == 301:
            return 0

    except requests.RequestException:
        return 0

    return 0


if __name__ == "__main__":
    if len(argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = argv[1]
        print("{:d}".format(number_of_subscribers(subreddit)))
