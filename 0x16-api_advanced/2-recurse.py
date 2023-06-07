#!/usr/bin/python3
"""
    This script queries the reddit API and returns a list containing the titles
    of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """ returns a list of all hot articles """

    url = "https://www.reddit.com/r/{}/top.json".format(subreddit)
    headers = {
        "User-Agent": "script for: 0x16.api.advanced: (by micoliser)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)
    if res.status_code == 404:
        print(None)

    data = res.json()["data"]
    after = data["after"]
    count += data["dist"]
    for child in data["children"]:
        hot_list.append(child["data"]["title"])

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
