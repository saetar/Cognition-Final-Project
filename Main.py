import LDA

lda = LDA.LDA_model("twitterLab/data/all_tweets.txt", 40)
lda.randomize_topics()
lda.train(10)

print(lda)