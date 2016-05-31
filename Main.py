import sys
import argparse
import scipy as sp
from scipy import stats

sys.path.insert(0, 'model')
import LDA

args = sys.argv


def help():
	print("An LDA model tester for tweets\n")

	print("Required arguments: alpha\tbeta\tnum_topics\ttraining")
	print("alpha: float between 0 and 1")
	print("beta: float betweeen 0 and 1")
	print("num_topics: number of topics in model (integer greater than 1)")
	print("training: number of training iterations (integer greater than 1)\n")

	print("Optional arguments: topics\tdocuments\tstats\thelp")
	print("topics: preview top 10 words from top 10 topics")
	print("documents: preview topic distribution for 10 documents of each hashtag")
	print("stats: cumulative comparison of topic distributions between different hashtag groups\n")

	print("help: get help again")
	sys.exit(0)


if len(args) < 4:
	help()

if float(args[1]):
	alpha = float(args[1])
	if alpha < 0 or alpha > 1:
		help()
else:
	help()

if float(args[2]):
	beta = float(args[2])
	if beta < 0 or beta > 1:
		help()
else:
	help()

if int(args[3]):
	num_topics = int(args[3])
	if num_topics < 1:
		help()
else:
	help()

if int(args[4]):
	training = int(args[4])
	if training < 1:
		help()
else:
	help()


if 'help' in args:
	help()
	sys.exit(0)

preview_topics = False
preview_documents = False
sts = False

if 'topics' in args:
	preview_topics = True

if 'documents' in args:
	preview_documents = True

if 'stats' in args:
	sts = True

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

lda = LDA.LDA_model(files, num_topics, alpha = alpha, beta = beta)

print("Training")
lda.train(training)
print("Done training")

if preview_topics:
	lda.preview_topics()

if preview_documents:
	lda.preview_documents()

if sts:
	m = lda.origin_topic_count()
	chisq, p, dof, expected = stats.chi2_contingency(m)
	print("Chi-square test of independence over topics and origins:")
	print(chisq, p, dof)
	print("Chi-square test of independence over categories and origins:")
	print(lda.eval_categories())