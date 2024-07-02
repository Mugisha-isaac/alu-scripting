#!/usr/bin/python3
"""
Python script that  returns a list containing the titles of all hot articles for a given subreddit.
 If no results are found for the given subreddit, the function should return None.
"""
import requests
from sys import argv


def recurse(subreddit, hot_list=[], after=None):
    """
    Function that queries the Reddit API and returns a list containing the titles of all hot articles
    for a given subreddit
    """
    url = "https://www.reddit.com/r/{subreddit}/hot.json".format(subreddit=subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data")
        children = data.get("children", [])
        hot_list.extend(children)
        after = data.get("after")
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return len(hot_list)

    else:
        return None


if __name__ == "__main__":
    subreddit = argv[1]
    print(recurse(subreddit))
