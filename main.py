#!/usr/local/bin/python3

from reddit import reddit
from submission import Submission


def submission_handler(submission):
    print(f'Title:\t\t{submission.title}')
    print(f'Score:\t\t{submission.score}')
    print(f'Author:\t\t{submission.author}')
    print(f'URL:\t\t{submission.url}')
    print(f'Thumbnail:\t{submission.thumbnail}')
    print(100 * '*')


def get_by_time_filter(sub_name, time_filter, limit, handler):
    for submission in reddit.subreddit(subreddit_name).top(time_filter=time_filter, limit=limit):
        handler(submission)


def stream_submissions(sub_name, handler):
    for submission in reddit.subreddit(subreddit_name).stream.submissions():
        handler(submission)


subreddit_name = 'all'
time_filter = 'week'
limit = 10

get_by_time_filter(subreddit_name, time_filter, limit, submission_handler)

# stream_submissions(subreddit_name, submission_handler)
