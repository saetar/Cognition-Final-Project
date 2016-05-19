'''
   Topic class.
   Authors: Daniel Lewitz & Ryan Saeta
'''

class Topic:
    def __init__(self):
        self.words = {}
        
    def add_word(self, word):
        if word in self.words:
            self.words[word] += 1
        else:
            self.words[word] = 1
        
    def get_words(self):
        return self.words
        
    def remove_word(self, word):
        if word in self.words:
            self.words[word] -= 1
        else:
            return -1
            
    def get_word_dist(self):
        total = 0
        dist_dict = {}
        for key in self.words:
            total += self.words[key]
        for key in self.words:
            dist_dict[key] = self.words[key]/total
        return dist_dict
    
    def calc_word_given_topic(self, word):
        return self.words.count(word)/len(self.words)