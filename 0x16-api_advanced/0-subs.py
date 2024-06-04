#!/usr/bin/python3
"""Module for task 0"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API
    Returns the number of subscribers (not active users, total subscribers)
    for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'Agent-Lix'})
    if response.status_code >= 300:
        return 0

    data = response.json()
    count = data.get('data').get('subscribers')
    return count
