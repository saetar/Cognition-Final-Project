import LDA
print("Loading corpus")
lda = LDA.LDA_model("twitterLab/data/my_life.txt", 20, alpha = .8, beta = .8)
"""print("Randomizing topics")
lda.randomize_topics()
print("Started Training")
lda.train(5)

print(lda)

documents = lda.get_documents()
for i in range(100):
    print(documents[i].get_topics(), documents[i].__str__())
    """
lda.train(20)
lda.preview()