# §/usr/bin/python3
"""recursive function"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """A recursive function that queries the Reddit
    API and returns a list containing the titles of all
    hot articles for a given subreddit. If no results
    are found for the given subreddit, the function should
    return None.
     Args:
        subreddit (str): subreddit

    Returns:
        int: number of subscribers
        """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    header = {"User-Agent": "my4rdRedditBot/4.0"}
    params = {"after": after} if after else {}

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
