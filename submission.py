from reddit import reddit
from datetime import datetime


class Submission():
    _id = None
    title = None
    author = None
    text = None
    created_at = None
    permalink = None
    score = None
    subreddit = None
    thumbnail = None
    url = None
    num_comments = None

    def __init__(self, s):
        self._id = s.id
        self.title = s.title
        self.author = s.author
        self.created_at = s.created
        self.permalink = s.permalink
        self.score = s.score
        self.subreddit = s.subreddit
        self.thumbnail = s.thumbnail
        self.url = s.url
        self.text = s.selftext
        self.num_comments = s.num_comments

    def __str__(self):
        return f'''
ID:\t\t{self._id}
Author:\t\t{self.author}
Created at:\t{datetime.fromtimestamp(int(self.created_at))}
Score:\t\t{self.score}
Comments:\t{self.num_comments}
Subreddit:\t{self.subreddit}
Thumbnail:\t{self.thumbnail}
URL:\t\t{self.url}
Permalink:\thttps://reddit.com{self.permalink}
Title:\t\t{self.title}
        '''

    def get_upvote_ratio(self):
        return reddit.submission(id=self._id).upvote_ratio
