#!/usr/bin/python3
"""
    This script queries the reddit API and returns the number of suscribers
    for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "script for: 0x16.api.advanced: (by micoliser)"
    }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        return 0
    subscribers = res.json().get("data").get("subscribers")

    return subscribers
