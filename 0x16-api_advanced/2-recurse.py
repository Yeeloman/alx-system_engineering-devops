# §/usr/bin/python3
"""recursive function"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """return the titles of the hot articles recursively
    subreddit is the target"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    header = {"User-Agent": "my4rdRedditBot/4.0"}
    params = {"after": after} if after else {}

    try:
        resp = requests.get(
            url,
            headers=header,
            params=params,
            allow_redirects=False
        )
        resp.raise_for_status()
        if resp.status_code == 200:
            data = resp.json()
            if "data" in data and "children" in data["data"]:
                for post in data["data"]["children"]:
                    hot_list.append(post["data"]["title"])
                if data["data"]["after"]:
                    return recurse(
                        subreddit,
                        hot_list,
                        after=data["data"]["after"]
                    )
                else:
                    return hot_list
        else:
            return None
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
