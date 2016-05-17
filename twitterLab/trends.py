"""Visualizing Tweets Across America

CS111, Winter 2016
Adapted from activity by Aditi Muralidharan and John DeNero.
 
"""

import data
import datetime
import sys
import geo
from maps import draw_state, draw_name, draw_dot, wait, message

# Part 1: Creating Tweets

def makeTweet(text, time, state):
    """Return a tweet, represented as a python dictionary.

    text  -- A string; the text of the tweet, all in lowercase
    time  -- A datetime object; the time that the tweet was posted.
             (You can ignore the time unless you get to the time extension.)
    state -- A string; the two digit abbreviation for the state where
               this tweet was tweeted
    """
    return {'text': text, 'time': time, 'state': state}

def tweetLocation(tweet):
    """Return the two letter abbreviation for the state where this tweet
    was posted."""
    pass # Delete this line and replace with your code!
    
    
def tweetTime(tweet):
    """Return the datetime that represents when the tweet was posted."""
    return tweet['time']

def tweetString(tweet):
    """Return a string representing the tweet."""
    return '"{0}" @ {1}'.format(tweet['text'], tweetLocation(tweet))

def getTweetWords(tweet):
    """Return a list of the words in the text of a tweet.
    This function should make use of the removeNonLetters
    method to include the words with no punctuation or numbers. Empty words
    (i.e., words that only consisted of punctuation and numbers) should not
    be included in the final list."""
    text = tweet['text']
    spaceSplit = text.split()
    words = []
    for word in spaceSplit:
        word = removeNonLetters(word)
        if len(word) > 0:
            words.append(word)
    return words


def removeNonLetters(string):
    """Return the string with punctuation and numbers removed, all all letters 
    lowercased. If all characters are punctuation and numbers, returns an empty 
    string. 
    """
    alphaString = ""
    for ch in string:
        if ch.isalpha():
            alphaString += ch
    return alphaString
    
def makeSampleTweets():
    """This function is only for testing purposes. It generates a short 
    list of tweets so that you can check whether your functions are working
    correctly. Three tweets are from Minnesota, and the other four
    included two from California, one from Maine, and one from Iowa."""
    sf = makeTweet("welcome to san francisco", None, "CA")
    berkeley = makeTweet("yay berkeley!", None, "CA")
    carleton = makeTweet("Welcome to Carleton :)", None, "MN")
    northfield = makeTweet("defeating jesse james", None, "MN")
    bemidji = makeTweet("Say hi to Paul and Babe", None, "MN")
    maine = makeTweet("Tweeting from Acadia National Park. Love the view!", None, "ME")
    iowa = makeTweet("getting ready to harvest corn #fun #tasty", None, "IA")
    return [sf, carleton, berkeley, northfield, maine, iowa, bemidji]
    
# Part 2: The Talk of the Nation

def groupTweetsByState(tweets):
    """Return a dictionary that aggregates tweets by their location.

    The keys of the returned dictionary are state abbreviations, and the values are
    lists of tweets that occurred in that state.

    tweets -- a sequence of tweets produced by the makeTweetFunction

    """
    pass # Delete this line and replace with your code!

    
def groupTweetCountsByState(term):
    """Returns a dictionary that aggregates counts of tweets by location.
    
    The keys of the returned dictionary are state abbreviations, and the values are
    the number of tweets containing term that occurred in that state.
    
    You'll want to call the function loadTweets in the module data. This function
    takes two parameters: the function for making tweets (makeTweet; just as for
    the pig homeworks, remember when passing a function as a parameter that we
    don't need parentheses after it - the parentheses call the function, whereas
    we actually want to pass in the function), and the term that you'd like to filter
    the tweets by. The function will only load tweets that include the given term.
    The call to this function has been included for you in the code below.
    
    Think about how you might use other functions you've written to make writing
    this function easier.

    term -- A string; this string will appear in all of the loaded tweets
    """
    tweets = data.loadTweets(makeTweet, term)
    pass # Delete this line and replace with your code!

         
         
# Part 3: The Mood of the Nation


    
def makeSentiment(value):
    """Return a sentiment, which represents a number between -1 and 1 or the value None.
    None means that there are no sentiment words in this tweet.
    """
    return {'sentiment': value}
    
def sentimentValue(s):
    """Return the value of a sentiment s.
    Results in an error if s does not have a sentiment.
    """
    assert hasSentiment(s), 'No sentiment value' # This line will crash the code if you call sentimentValue with a None sentiment
    return s.get('sentiment')

def hasSentiment(s):
    """Return a boolean indicating whether sentiment s has a value.
    If the sentiment value is None, return False, otherwise return True.
    
    Look at the makeSentiment method to see if how sentiments are represented
    - the input to this function is the output of that function.
    
    """
    pass # Delete this line and replace with your code!
   

def getWordSentiment(word):
    """Return a sentiment representing the degree of positive or negative
    feeling in the given word.
    """
    return makeSentiment(data.word_sentiments.get(word))#data.word_sentiments is the dictionary of sentiment values

def analyzeTweetSentiment(tweet):
    """ Return a sentiment representing the degree of positive or negative
    sentiment in the given tweet, averaging over all the words in the tweet
    that have a sentiment value.

    If no words in the tweet have a sentiment value, return
    makeSentiment(None). Otherwise, return the result of makeSentiment
    with the average sentiment value. 
    
    Code note: You'll need to keep track of how many words have sentiment
    to properly compute the average.
    """
    pass # Delete this line and replace with your code!

def averageSentiments(tweetsByState):
    """Calculate the average sentiment of the states by averaging over all
    the tweets from each state. Return the result as a dictionary from state
    names to average sentiment values (numbers).

    If a state has no tweets with sentiment values, leave it out of the
    dictionary entirely.  Do NOT include states with no tweets, or with tweets
    that have no sentiment, as 0.  0 represents neutral sentiment, not unknown
    sentiment.

    tweetsByState -- A dictionary from state names to lists of tweets
    """
    pass # Delete this line and replace with your code!
    
def calculateAverageSentiments(listOfTweets):
    """Calculates the average sentiment over all tweets in the list. The average
    sentiment is the sum of all of the sentiments with a value, divided by the
    total number of tweets with a sentiment. 
    
    If the list is empty or if it has no tweets with a sentiment, return None;
    otherwise, return the average.
    """
    pass # Delete this line and replace with your code!

# Optional extensions: Grouping by time

def groupTweetsByHour(tweets):
    """Return a dictionary that groups tweets by the hour they were posted.

    The keys of the returned dictionary are the integers 0 through 23.

    The values are lists of tweets, where tweets_by_hour[i] is the list of all
    tweets that were posted between hour i and hour i + 1. Hour 0 refers to
    midnight, while hour 23 refers to 11:00PM.

    To get started, read the Python Library documentation for datetime objects:
    http://docs.python.org/py3k/library/datetime.html#datetime.datetime

    tweets -- A list of tweets to be grouped
    """
    pass # Delete this line and replace with your code!



# Interaction.  You don't need to read this section of the program.

def printSentiment(text='Are you virtuous or verminous?'):
    """Print the words in text, annotated by their sentiment scores."""
    tweet = makeTweet(text, None, '')
    words = getTweetWords(tweet)
    layout = '{0:>' + str(len(max(words, key=len))) + '}: {1:+}'
    for word in words:
        s = getWordSentiment(word)
        if hasSentiment(s):
            print(layout.format(word, sentimentValue(s)))

def drawCenteredMap(center_state='TX', n=10):
    """Draw the n states closest to center_state."""
    us_centers = {n: geo.find_center(s) for n, s in geo.us_states.items()}
    center = us_centers[center_state.upper()]
    dist_from_center = lambda name: geo.geo_distance(center, us_centers[name])
    for name in sorted(geo.us_states.keys(), key=dist_from_center)[:int(n)]:
        draw_state(geo.us_states[name])
        draw_name(name, us_centers[name])
    draw_dot(center, 1, 10)  # Mark the center state with a red dot
    wait()

def drawStateSentiments(state_sentiments):
    """Draw all U.S. states in colors corresponding to their sentiment value.

    Unknown state names are ignored; states without values are colored grey.

    state_sentiments -- A dictionary from state strings to sentiment values
    """
    for name, shapes in geo.us_states.items():
        sentiment = state_sentiments.get(name, None)
        draw_state(shapes, sentiment)
    for name, shapes in geo.us_states.items():
        center = geo.find_center(shapes)
        if center is not None:
            draw_name(name, center)
            
def drawStateCounts(countsByState):
    """Draw all U.S. states in colors corresponding to their sentiment value.

    Unknown state names are ignored; states without values are colored grey.

    countsByState - a dictionary with keys that are states, values are number
    of tweets with that count.
    """
    # First, scale the counts into -1 - +1 range. minimum will be at -1, maximum
    # will be at +1
    minTweets = 9999999999999
    maxTweets = -1
    for state in countsByState:
        count = countsByState[state]
        if count > maxTweets:
            maxTweets = count
        if count < minTweets:
            minTweets = count
    # Now, each states "count" will be (count - minTweets)/(maxTweets-minTweets)*2 - 1
    # This ensures minTweets will be at -1 and max at +1. If maxTweets - minTweets = 0,
    # set all counts to 0.
    scaledCountsByState = {} # Create a new dictionary to avoid modifying the old one
    for state in countsByState:
        if maxTweets - minTweets != 0:
            count = countsByState[state]
            scaledCountsByState[state] = 2*(count - minTweets)/(maxTweets-minTweets) - 1
        else:
            scaledCountsByState[state] = 0
    
    for name, shapes in geo.us_states.items():
        sentiment = scaledCountsByState.get(name, None)
        draw_state(shapes, sentiment)
    for name, shapes in geo.us_states.items():
        center = geo.find_center(shapes)
        if center is not None:
            draw_name(name, center)

def drawMapForTerm(term='my job'):
    """Draw the sentiment map corresponding to the tweets that contain term.

    Some term suggestions:
    New York, Texas, sandwich, my life, justinbieber
    """
    tweets = data.loadTweets(makeTweet, term)
    tweets_by_state = groupTweetsByState(tweets)
    state_sentiments = averageSentiments(tweets_by_state)
    drawStateSentiments(state_sentiments)
    wait()

def drawCountsMapForTerm(term='my job'):
    """Draw the counts map corresponding to the tweets that contain term.

    Some term suggestions:
    New York, Texas, sandwich, my life, justinbieber
    """
    countsByState = groupTweetCountsByState(term)
    drawStateCounts(countsByState)
    wait()

def drawMapByHour(term='my job', pause=0.5):
    """Draw the sentiment map for tweets that match term, for each hour."""
    tweets = data.loadTweets(makeTweet, term)
    tweets_by_hour = groupTweetsByHour(tweets)

    for hour in range(24):
        current_tweets = tweets_by_hour.get(hour, [])
        tweets_by_state = groupTweetsByState(current_tweets)
        state_sentiments = averageSentiments(tweets_by_state)
        drawStateSentiments(state_sentiments)
        message("{0:02}:00-{0:02}:59".format(hour))
        wait(pause)


def main(*args):
    """Read command-line arguments and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Run Trends")
    parser.add_argument('--printSentiment', '-p', action='store_true')
    parser.add_argument('--drawCenteredMap', '-d', action='store_true')
    parser.add_argument('--drawMapForTerm', '-m', action='store_true')
    parser.add_argument('--drawMapByHour', '-b', action='store_true')
    parser.add_argument('--drawCountsMapForTerm', '-c', action='store_true')
    parser.add_argument('text', metavar='T', type=str, nargs='*',
                        help='Text to process')
    args = parser.parse_args()
    for name, execute in args.__dict__.items():
        if name != 'text' and execute:
            globals()[name](' '.join(args.text))

if __name__=="__main__":
    '''Call the main function, passing the command line arguments in as parameters'''
    main(sys.argv[1:])

