# §/usr/bin/python3
"""recursive function"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """return the titles of the hot articles recursively
    subreddit is the target
     Args:
        subreddit (str): subreddit

    Returns:
        int: number of subscribers
        """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'custom'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        r = r.json()
        for post in r.get('data').get('children'):
            hot_list.append(post.get('data').get('title'))
        if r.get('data').get('after'):
            recurse(subreddit, hot_list)
        return hot_list
    else:
        return None
