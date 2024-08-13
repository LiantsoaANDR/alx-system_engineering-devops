#!/usr/bin/python3
"""Module for task 1"""

import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'Agent-Lix'})
    if response.status_code >= 300:
        print("None")
        return

    data = response.json()
    posts = data.get('data').get('children')
    for p in posts:
        title = p.get('data').get('title')
        print(title)
