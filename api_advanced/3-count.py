#!/usr/bin/python3
""" 3-count.py """

import re
import requests
from collections import defaultdict
from sys import argv


def count_words(subreddit, word_list, hot_list=None, after=None):
    """
    Recursively queries the Reddit API to retrieve the titles of all hot articles
    in the specified subreddit and counts the occurrence of each keyword.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to count.
        hot_list (list, optional): A list to store hot article titles. Defaults to None.
        after (str, optional): The "after" parameter for pagination. Defaults to None.

    Returns:
        None: Prints the sorted word count of keywords.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 100, "after": after}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json().get("data", {})
        except ValueError:
            print(f"Error: Unable to parse JSON response from {url}")
            return

        children = data.get("children", [])
        hot_list.extend(children)

        after = data.get("after")
        if after:
            return count_words(subreddit, word_list, hot_list, after)
        else:
            return process_titles(hot_list, word_list)
    elif response.status_code == 404:
        print(f"Error 404: Subreddit {subreddit} not found.")
        return
    else:
        print(f"Error {response.status_code}: {response.text}")
        return


def process_titles(hot_list, word_list):
    """
    Processes the titles of hot articles to count the occurrences of specified keywords.

    Args:
        hot_list (list): A list of hot articles.
        word_list (list): A list of keywords to count.

    Returns:
        None: Prints the sorted word count of keywords.
    """
    word_count = defaultdict(int)
    word_set = {word.lower() for word in word_list}

    for post in hot_list:
        title = post.get("data", {}).get("title", "")
        words = re.findall(r"\b\w+\b", title.lower())
        for word in words:
            if word in word_set:
                word_count[word] += 1

    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_word_count:
        if count > 0:
            print(f"{word}: {count}")


if __name__ == "__main__":
    if len(argv) < 3:
        print(
            'Usage: python3 script.py <subreddit> "<keyword1> <keyword2> ... <keywordN>"'
        )
    else:
        subreddit = argv[1]
        word_list = argv[2].split()
        count_words(subreddit, word_list)
