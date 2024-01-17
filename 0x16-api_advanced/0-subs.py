#!/usr/bin/python3
"""task 0"""
import requests


def number_of_subscribers(subreddit):
    """return number of subs in an existing account"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyFirstRedditBot/1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        if response.status_code == 200:
            data = response.json()
            return data["data"]["subscribers"]
        else:
            return 0
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        return 0
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
        return 0
