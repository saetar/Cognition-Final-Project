'''
   Helper functions for tweets and Tweet class.
   Authors: Daniel Lewitz & Ryan Saeta
'''

import re

class Tweet:
    def __init__(self, place="", text="", date=""):
        '''
        Initialize Tweet object with place, text, and date.
        Creates hashtag and cleans text.
        '''
        self.place = place
        self.text = self.clean_text(text)
        self.date = date
        
    def clean_text(self,text):
        '''
        Takes text and removes hashtags, @'s, links, and punctuation.
        Also removes stop words and words that have fewer than 3 letters. 
        '''
        stops = self.load_stops('data/stop_words.txt')
        new_txt = []
        txt = text.split()
        rx = re.compile('\W+')        
        for w in txt:
            n_w = w.lower()
            n_w = rx.sub('', n_w).strip()
            if 'http' in n_w:
                txt.remove(w)
            elif '#' in n_w:
                txt.remove(w)
            elif n_w in stops:
                txt.remove(w)
            elif not n_w.isalpha():
                txt.remove(w)
            elif len(n_w) <= 2:
                txt.remove(w)
            else:
                new_txt.append(n_w)
        s = ''
        for w in new_txt:
            s += w + " "
        return s
    
    def load_stops(self, filename):
        '''
        Loads a list of stop words to ignore in tweets from filename.
        '''
        f = open(filename, 'r')
        stops = []
        for l in f.readlines():
            if not l[0] == '(':
                stops.append(l.strip())
        return stops
    
    def set_place(self, place):
        self.place = place
        
    def set_text(self, text):
        self.text = text
        
    def set_origin(self, origin):
        self.origin = origin
        
    def get_origin(self):
        return self.origin
        
    def get_words(self):
        return self.text.split()
        
    def set_date(self, date):
        self.date = date
        
    def get_text(self):
        return self.text
    
    def get_place(self):
        return self.place
    
    def get_date(self):
        return self.date
                  
    def __str__(self):
        return "(" + self.place + ", " + self.text + ", " + self.date + ")"        