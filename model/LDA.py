from tweets import Tweet
from Document import Document
from topics import Topic
import numpy as np
from collections import Counter
import scipy as sp

class LDA_model:
    def __init__(self, documents_filepaths, k, alpha =.5, beta =.5):
        self.k = k
        self.documents = self.get_docs(documents_filepaths, "\t")
        self.V = []
        for doc in self.documents:
            words = doc.get_tweet_words()
            for word in words:
                if not word in self.V:
                    self.V.append(word)
        self.doc_topic_counts = np.zeros((len(self.documents), k)) + alpha
        self.topics = np.zeros((k, len(self.V))) + beta
        self.topic_word_counts = np.zeros(k) + len(self.V)*beta
        for i in range(len(self.documents)):
            document = self.documents[i]
            topics_list = []
            for word in document.get_tweet_words():
                assignment = np.random.randint(0,k)
                self.topic_word_counts[assignment] +=1
                topics_list.append(assignment)
                self.doc_topic_counts[i,assignment] += 1
                self.topics[assignment, self.V.index(word)] +=1
            document.set_topics(topics_list)

                

        
    def get_docs(self, filepaths, delimiter):
        tweets = []
        for filepath in filepaths:
            f = open(filepath, 'r')
            for l in f.readlines():
                line = l.strip().split(delimiter)
                if len(line) ==3:
                    tweet = Tweet(place=line[0], text=line[2], date=line[1])
                    if len(tweet.get_words()) > 3:
                        tweet.set_origin(filepath)
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
    #Gibbs sampling
        for i in range(len(self.documents)):
            document = self.documents[i]
            topics_list = document.get_topics()
            word_list = document.get_tweet_words()
            for j in range(len(word_list)):
                assignment = topics_list[j]
                word = word_list[j]
                self.doc_topic_counts[i, assignment] -=1
                self.topics[assignment, self.V.index(word)] -=1
                self.topic_word_counts[assignment] -=1 
                
                p = self.topics[:, self.V.index(word)]
                p = self.doc_topic_counts[i] * p
                p =  p / self.topic_word_counts
                
                new_assignment = np.random.multinomial(1, p/p.sum()).argmax()
                

                
                self.doc_topic_counts[i, new_assignment] +=1
                self.topics[new_assignment, self.V.index(word)] +=1
                self.topic_word_counts[new_assignment] +=1   
                topics_list[j] = new_assignment
            document.set_topics(topics_list)
                
    
    def train(self, num_iters):
        for i in range(num_iters):
#            print(i)
            self.improve_topics()
            
    def get_documents(self):
        return self.documents
        
    def categorize_documents(self):
        cat_docs = []
        for doc in self.documents:
            counts = Counter(doc.get_topics())
            most_common = counts.most_common()[0][0]
            cat_docs.append((doc, most_common))
        return cat_docs
            
    def origin_categories(self):
        d = {}
        cat_docs = self.categorize_documents()
        for doc, common in cat_docs:
            origin = doc.get_origin()
            if origin in d:
                d[origin].append(common)
            else:
                d[origin] = [common]
        return d
        
    def eval_categories(self):
        ps = []
        d = self.origin_categories()
        for origin, lst in d.items():
            chisq, p = sp.stats.chisquare(lst)
            ps.append((origin, p))
            
        return ps
            
        
    def __str__(self):
        s = ""
        for t in self.topics:
            s += t.__str__() + "\n"
            
        return s
        
    def preview_topics(self):
        for i in range(min(10, len(self.topics))):
            topic = self.topics[i]
            argsort = topic.argsort()
            indicies = argsort[-10:]
            words = [str((self.V[j] , int(self.topics[i,j]))) for j in indicies]
            output = "Topic {}: {}".format(i, ' '.join(words))
            print(output)
            
    def get_origin_dict(self, doc_limit=None):
        origins_dict = {}
        for doc in self.documents:
            doc_origin = doc.get_origin()
            if not doc_origin in origins_dict:
                origins_dict[doc_origin] = [doc]
            else:
                if doc_limit:
                    if len(origins_dict[doc_origin]) < doc_limit:
                        origins_dict[doc_origin].append(doc)
                else:
                    origins_dict[doc_origin].append(doc)        
        return origins_dict
            
    def preview_documents(self):
        origins_dict = self.get_origin_dict(doc_limit=10)              
        for key, value in origins_dict.items():
            print("Origin: ", key)
            for i, val in enumerate(value):
                #print(i, val.__str__())
                print('\t', val.get_topics())
                
    def origin_topic_count(self):
        origins_dict = self.get_origin_dict()
        counts = [] 
        for origin, docs in origins_dict.items():
            count = list(np.zeros(self.k))
            for doc in docs:
                topics = doc.get_topics()
                for topic in topics:
                    count[topic] += 1
            counts.append(count)            
        return counts
                