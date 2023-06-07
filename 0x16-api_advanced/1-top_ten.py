#!/usr/bin/python3
"""
    This script queries the reddit API and prints the titles of the first
    10 hot posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    """ prints the titles of first 10 hot posts """

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "script for: 0x16.api.advanced: (by micoliser)"
    }
    params = {
        "limit": 10
    }
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)
    if res.status_code == 404:
        print(None)
        return

    data = res.json().get("data")
    for child in data.get("children"):
        print(child.get("data").get("title"))
