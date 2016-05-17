'''
   Topic class.
   Authors: Daniel Lewitz & Ryan Saeta
'''

import tweets
import topics
import random

class Document:
    def __init__(self, tweet):
        self.tweet = tweet
        
    def set_topics(self, topics):
        self.topics = topics
        
    def set_tweet(self, tweet):
        self.tweet = tweet
        
    def randomize(topics_list):
        '''
            Initial random assignment of words in d to topics
        '''
        for word in self.tweet.get_text():
            topics_list[random.randint(0,len(topics_list))].add_word(word)
        return topics_list
    
    def calculate_topic_distribution(self, topic):
        '''
            Calculate single instance of p(topic t | document d)
        '''
        txt = self.tweet.get_text()
        topic_words = topic.get_words()
        count = 0
        for word in topic_words:
            if word in txt:
                count += 1
                
        return count/len(txt)
    
    def calculate_topics_distribution(self, topics):
        '''
            Calculate distribution of p(topic t | document d)'s 
        '''
        topics_distribution = []
        sm = 0
        for topic in topics:
            result = calculate_topic_distribution(topic)
            sm += result
            topics_distribution.append(result)
            
        return [i/sm for i in topics_distribution]
    
    