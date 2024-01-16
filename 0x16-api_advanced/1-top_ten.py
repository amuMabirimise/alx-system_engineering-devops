#!/usr/bin/python3
"""
Contains the top_ten function
"""
import requests


def top_ten(subreddit):
    """prints the titles of the top ten hot posts for a given subreddit"""
    url = f'http://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Python/requests:APIproject:v1.0.0 (by /u/aaorrico23)'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses

        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            print(None)
        else:
            for post in posts:
                print(post.get('data', {}).get('title', None))

    except requests.exceptions.HTTPError as e:
        if response.status_code == 403:
            print(f"Error: 403 Client Error: Blocked for url: {url}. Unable to fetch posts for subreddit '{subreddit}'.")
        else:
            print(f"Error: {e}. Unable to fetch posts for subreddit '{subreddit}'.")

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        top_ten(subreddit_name)
