'''
   Topic class.
   Authors: Daniel Lewitz & Ryan Saeta
'''

from tweets import Tweet
from topics import Topic
import random

class Document:
    def __init__(self, tweet):
        self.tweet = tweet
        self.topics = []
        
    def set_topics(self, topics):
        self.topics = topics
        
    def set_tweet(self, tweet):
        self.tweet = tweet
        
    def __str__(self):
        return self.tweet.__str__()
        
    def randomize(self, topics_list):
        '''
            Initial random assignment of words in d to topics
        '''
        words = self.tweet.get_words()
        for i in range(len(words)):
            assignment = random.randint(0, len(topics_list) - 1)
            self.topics.append(assignment)
            topics_list[assignment].add_word(words[i])
        return topics_list
    
    def reassign(self, topics_list):
        words = self.tweet.get_words()
        for i in range(len(words)):
            self.topics[i] = -1
            topics_distribution = self.calculate_topics_distribution(topics_list)
            word_distribution = self.calculate_word_distribution(topics_list, words[i])
            prob_topics = []
            for j in range(len(topics_distribution)):
                prob_topics.append(topics_distribution[j] * word_distribution[j])
                
            if not sum(prob_topics) == 0:
                prob_topics = [prob_topic/sum(prob_topics) for prob_topic in prob_topics]
            assignment = random.random()
            p = 0.
            index = -1
            while p < assignment:
                index += 1
                p += prob_topics[index]
            self.topics[i] = index
            topics_list[index].add_word(words[i])
        return topics_list
    
    def calculate_topic_distribution(self, topic_index):
        '''
            Calculate single instance of p(topic t | document d) ignoring current word
        '''
        return self.topics.count(topic_index)/(len(self.topics)-1)
    
    def calculate_topics_distribution(self, topics):
        '''
            Calculate distribution of p(topic t | document d)'s 
            Length = len(topics_list)
        '''
        topics_distribution = []
        for topic in range(len(topics)):
            result = self.calculate_topic_distribution(topic)
            topics_distribution.append(result)
            
        return topics_distribution
    
    def calculate_word_distribution(self, topics_list, word):
        '''
            p(word w | topic t)
            Length = len(topics_list)
        '''
        
        word_dist = []
        for topic in topics_list:
            if word in topic.get_word_dist():
                word_dist.append(topic.get_word_dist()[word])
            else:
                word_dist.append(0)
        return word_dist
                
        #return 
        #[topic.get_word_dist()[word] for topic in topics_list]