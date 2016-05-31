from tweets import Tweet
from Document import Document

import numpy as np
from collections import Counter
import scipy as sp

class LDA_model:
    """Sets the paramters of the model, and loads the all of the tweets from the given files"""
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
        ''' 
        Takes a list of files and a delimiter and returns a list of 
        tweet objects. 
        '''
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
        '''
        Takes a list of Tweet objects and returns a list of Document objects,
        each containing one tweet.
        '''
        docs = []
        for tweet in tweets:
            docs.append(Document(tweet))
        return docs
        
        
    def improve_topics(self):
        """One iteration of Gibbs sampling for each word w in document d,
        forgets current topic assignment, and chooses new one with probability
        of assignment to topic t proportional to p(t | d)p(w |t)"""
        
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
        '''
        Improves topics num_iteres times.
        '''
        for i in range(num_iters):
            self.improve_topics()
        
    def categorize_documents(self):
        '''
        Creates a list of (category, document) tuples where the
        category is the most most frequent topic assignment accross
        words in document.
        '''
        cat_docs = []
        for doc in self.documents:
            counts = Counter(doc.get_topics())
            most_common = counts.most_common()[0][0]
            cat_docs.append((doc, most_common))
        return cat_docs
            
    def origin_categories(self):
        '''
        Creates a dictionary where keys are the origins and values
        are lists of categories from documents of that origin. 
        '''
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
        '''
        Evaluates category assignments by using a chi-squared test
        of independence for categories of the same origin.
        '''
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
        '''
        Displays 10 most common words in first 10 (or fewer) topics.
        '''
        for i in range(min(10, len(self.topics))):
            topic = self.topics[i]
            argsort = topic.argsort()
            indicies = argsort[-10:]
            #words = [str((self.V[j] , int(self.topics[i,j]))) for j in indicies]
            words = [str(self.V[j]) for j in indicies]
            output = "Topic {}: {}".format(i, ', '.join(words))
            print(output)
            
    def get_origin_dict(self, doc_limit=None):
        '''
        Creates a dictionary where keys are hashtags and values are lists of documents
        pertaining to that hashtag.
        '''
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
        '''
        Displays topic assignments for each word in first 10 documents of each origin.
        '''
        origins_dict = self.get_origin_dict(doc_limit=10)              
        for key, value in origins_dict.items():
            print("Origin: ", key)
            for i, val in enumerate(value):
                #print(i, val.__str__())
                print('\t', val.get_topics())
                
    def origin_topic_count(self):
        '''
        Creates a list for each origin where each element is a count of the words assigned
        to each topic. Element[i,j] is the number of words in origin i assigned to topic j
        '''
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
                
