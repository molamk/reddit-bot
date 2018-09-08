# How to build a Reddit bot?

## Prerequisites

```bash
# Create a Reddit app and grab your credenials
pip3 install python-dotenv praw
```

## Environment setup

```bash
# Create an .env file, it should look like this
CLIENT_SECRET=<YOUR_APP_SECRET>
CLIENT_ID=<YOUR_APP_ID>
USER_AGENT=<platform>:<app name>:<version> (by /u/<username>)
```

## Authenticate your app

```python
import dotenv
import os
import praw

# Load the environment variables
dotenv.load_dotenv()

# Authenticate the app
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent=os.getenv("CLIENT_USER_AGENT"))
```

## Handle a submission (basic printing)

```python
def submission_handler(submission):
    print(f'Title:\t\t{submission.title}')
    print(f'Score:\t\t{submission.score}')
    print(f'Author:\t\t{submission.author}')
    print(f'URL:\t\t{submission.url}')
    print(f'Thumbnail:\t{submission.thumbnail}')
    print(100 * '*')
```

## Get submissions by time filter

```python
subreddit_name = 'all'
time_filter = 'week'
limit = 10

get_by_time_filter(subreddit_name, time_filter, limit, submission_handler)
```

## Stream submissions in real-time

```python
subreddit_name = 'all'

stream_submissions(subreddit_name, submission_handler)
```

## Useful links

- [PRAW](https://praw.readthedocs.io/en/latest/)
- [The 12 factor app](https://12factor.net/)
