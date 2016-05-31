required input:

python Main.py alpha beta num_topics num_training_iterations

alpha: float between 0 and 1

beta: flaot between 0 and 1

num_topics: int greater than 1. recommended ~10

num_training_iterations: positive int. recommended range 25-125

passing in this alone will create an LDA model, but will not display anything. to display information about the results of the model, can also add after the required arguments to the commandline:

topics: preview top 10 words from top 10 topics

documents: preview topic distribution for 10 documents of each hashtag

stats: cumulative comparison of topic distributions between different hashtag groups
