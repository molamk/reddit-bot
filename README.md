# How to build a Reddit bot?

## Prerequisites
1. Head over to [Reddit](https://www.reddit.com)
1. Go to: Preferences -> Create App

## Environment configuration
```bash
# PRAW for reddit, dotenv for the env variables
$ pip3 install praw python-dotenv
# Create a file to store your environment variables
$ touch .env
# CLIENT_SECRET=<YOUR_APP_SECRET>
# CLIENT_ID=<YOUR_APP_ID>
# USER_AGENT=<platform>:<app name>:<version> (by /u/<username>)
```

## App setup
```python
from dotenv import load_dotenv
import os
import praw

# Load configuration
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
CLIENT_USER_AGENT = os.getenv("CLIENT_USER_AGENT")

# Authenticate the app
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=CLIENT_USER_AGENT)
```

## Run
```python
subreddit_name = 'deepfriedmemes'
time_filter = 'week'
limit = 10

for submission in reddit.subreddit(subreddit_name).top(time_filter=time_filter, limit=limit):
    print(f'Title:\t\t{submission.title}')
    print(f'Score:\t\t{submission.score}')
    print(f'Author:\t\t{submission.author}')
    print(f'URL:\t\t{submission.url}')
    print(f'Thumbnail:\t{submission.thumbnail}')
    print(100 * '*')
```

## Useful links
- [PRAW](https://praw.readthedocs.io/en/latest/)
- [The 12 factor app](https://12factor.net/)
