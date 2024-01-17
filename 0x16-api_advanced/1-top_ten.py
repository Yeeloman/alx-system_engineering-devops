#!/usr/bin/python3
"""2- top ten"""

import requests


def top_ten(subreddit):
    """return top 10 hot posts for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MySecndRedditBot/1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        if response.status_code == 200:
            data = response.json()
            if "data" in data and "children" in data["data"]:
                for post in data["data"]["children"]:
                    print(post["data"]["title"])
            else:
                print("None")
        else:
            print("Invalid subreddit or other error")
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
