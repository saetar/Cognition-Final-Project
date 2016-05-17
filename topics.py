'''
   Topic class.
   Authors: Daniel Lewitz & Ryan Saeta
'''

class Topic:
    def __init__(self):
        self.words = []
        
    def add_word(self, word):
        self.words.append(word)
        
    def get_words(self):
        return self.words
    
    def calc_word_given_topic(self, word):
        return self.words.count(word)/len(self.words)