import sys
sys.path.insert(0, 'model')

import scipy as sp
from scipy import stats
import LDA
print("Loading corpus")
files = [
    "data/tweets/ss2016.txt", 
    "data/tweets/blm.txt", 
    "data/tweets/hb2.txt", 
    "data/tweets/indy500.txt", 
    "data/tweets/okcvgsw.txt", 
    "data/tweets/science.txt",
    "data/tweets/blm_old.txt",
    "data/tweets/science_recent.txt",
    "data/tweets/hb2_recent.txt"
]
lda = LDA.LDA_model(files, 6, alpha = 0.01, beta = .01)

print("Training")
lda.train(100)
print("Done training")
lda.preview_topics()
lda.preview_documents()
m = lda.origin_topic_count()
chisq, p, dof, expected = stats.chi2_contingency(m)
print(chisq, p, dof)
#chisq_p = 1 - sp.stats.chi2cd(chisq, (len(m) - 1)*(len(m[0]) - 1))
#print(chisq_p)
print(lda.eval_categories())