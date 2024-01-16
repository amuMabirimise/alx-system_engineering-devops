#!/usr/bin/python3

import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditClient/1.0"}

    try:
        response = requests.get(url, headers=headers, params={'limit': 10}, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()

            if 'data' in data and 'children' in data['data']:
                for post in data['data']['children']:
                    title = post['data']['title']
                    print(title)
            else:
                print(f"No posts found for subreddit '{subreddit}'.")

        elif response.status_code == 403:
            print(f"Access to subreddit '{subreddit}' is forbidden.")
        elif response.status_code == 302:
            print(f"Redirect for subreddit '{subreddit}'. Invalid subreddit.")
        else:
            print(f"Error: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

