import json
import sys

def make_tweets(filename):
	tweet_texts = []
	f = open(filename, 'r')
	fjson = json.load(f)
	for status in fjson["statuses"]:
		tweet_texts.append(status["text"])

	return tweet_texts

def main(args):
	print("Made it bois")
	tweets = make_tweets(args[1])
	outputfile = open(args[2], 'w')
	print(len(tweets))
	for tweet in tweets:
		outputfile.write("BS\tBS\t" + tweet + '\n')

if __name__ == "__main__":
	args = sys.argv
	main(args)