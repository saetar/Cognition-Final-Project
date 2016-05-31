'''
   Topic class.
   Authors: Daniel Lewitz & Ryan Saeta
'''

from tweets import Tweet
import random

class Document:
    def __init__(self, tweet):
        '''
        Initialize Document object with Tweet object
        '''
        self.tweet = tweet
        self.topics = []
        self.origin = tweet.get_origin()
        
    def set_topics(self, topics):
        self.topics = topics
        
    def set_tweet(self, tweet):
        self.tweet = tweet
    
    def get_tweet_words(self):
        return self.tweet.get_words()
        
    def __str__(self):
        return self.tweet.__str__()
    
    def get_topics(self):
        return self.topics
        
    def get_origin(self):
        return self.origin