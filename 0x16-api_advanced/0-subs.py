#!/usr/bin/python3
"""Function of query subscribers on a given Reddit subreddit."""
#!/usr/bin/python3
"""Function of query subscribers on a given Reddit subreddit."""
import requests
import time


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "CustomUserAgent/1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        time.sleep(2)

        if response.status_code == 200:
            data = response.json()
            subscribers_count = data['data']['subscribers']
            return subscribers_count

        elif response.status_code == 302:
            print(f"Redirect for subreddit '{subreddit}'. Invalid subreddit.")
            return 0

        elif response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
            return 0

        else:
            print(f"Error: {response.status_code}")
            return 0

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return 0


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        subscribers_count = number_of_subscribers(subreddit_name)
        print(f"{subreddit_name} has {subscribers_count} subscribers.")
