'''
   Helper functions for tweets and Tweet class.
   Authors: Daniel Lewitz & Ryan Saeta
'''

import re

class Tweet:
    def __init__(self, place="", text="", date=""):
        self.place = place
        self.text = self.clean_text(text)
        self.date = date
        self.hashtag = self.get_hashtag(self.text)
        
    def clean_text(self,text):
        stops = self.load_stops('stop_words.txt')
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
    
    def get_hashtag(self, text):
        hashtag = ""
        in_hashtag = False
        for letter in text:
            if in_hashtag:
                if letter == " ":
                    in_hashtag = False
                    break
                else:
                    hashtag += letter
            if letter == "#":
                in_hashtag = True
                
        return hashtag
                
    
    def __str__(self):
        return "(" + self.place + ", " + self.text + ", " + self.date + ")"
        
    

def load_tweets(filename, delimiter):
    tweets = []
    f = open(filename, 'r')
    for l in f.readlines():
        line = l.strip().split(delimiter)
        tweet = Tweet(place=line[0], text=line[1], date=line[2])
        tweets.append(tweet)
        
    return tweets

if __name__ == "__main__":
    tweets = load_tweets("twitterLab/data/mn.txt", "\t")
    print("We have", len(tweets), "tweets")
    print(tweets[10])