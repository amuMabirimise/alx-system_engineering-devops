#!/usr/bin/python3

import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditClient/1.0"}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    try:
        response = requests.get(url, headers=headers, 
                params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            if not posts:
                return hot_list

            titles = [post['data']['title'] for post in posts]
            hot_list.extend(titles)

            after = data.get('data', {}).get('after')
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list

        elif response.status_code == 302:
            print(f"Redirect for subreddit '{subreddit}'. Invalid subreddit.")
            return None

        else:
            print(f"Error: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return None


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
