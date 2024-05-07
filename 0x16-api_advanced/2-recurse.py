#!/usr/bin/python3post_list
"""Module for task 2"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    queries the Reddit API and returns a list containing the titles of
    all hot articles for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 100}
    headers = {'User-Agent': 'Agent-Lix'}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code >= 300:
        return None

    data = response.json()
    post_list = data.get('data').get('children')
    if not post_list:
        return hot_list

    for post in post_list:
        hot_list.append(post['data']['title'])

    after = data.get('data').get('after')

    if after is not None:
        return recurse(subreddit, hot_list)
    return hot_list
