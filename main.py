#!/usr/local/bin/python3

from reddit import reddit
from submission import Submission

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
