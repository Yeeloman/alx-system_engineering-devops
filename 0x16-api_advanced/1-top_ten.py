#!/usr/bin/python3
"""2- top ten"""

import requests


def top_ten(subreddit):
    """A function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MySecndRedditBot/1.0"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if "data" in data and "children" in data["data"]:
            for post in data["data"]["children"]:
                print(post["data"]["title"])
        else:
            print("None")
    else:
        print("Invalid subreddit or other error")
