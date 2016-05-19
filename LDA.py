from tweets import Tweet
from Document import Document
from topics import Topic

class LDA_model:
    def __init__(self, documents_filepath, k):
        self.documents = self.get_docs(documents_filepath, "\t")
        self.topics = [Topic() for i in range(k)]
        
    def get_docs(self, filepath, delimiter):
        tweets = []
        f = open(filepath, 'r')
        for l in f.readlines():
            line = l.strip().split(delimiter)
            tweet = Tweet(place=line[0], text=line[2], date=line[1])
            tweets.append(tweet)
        return self.make_documents(tweets)
        
    def make_documents(self, tweets):
        docs = []
        for tweet in tweets:
            docs.append(Document(tweet))
        return docs
    
    def randomize_topics(self):
        for document in self.documents:
            self.topics = document.randomize(self.topics)
        
        
    def improve_topics(self):
        for document in self.documents:
            self.topics = document.reassign(self.topics)
    
    def train(self, num_iters):
        for i in range(num_iters):
            self.improve_topics()
            
    def get_documents(self):
        return self.documents