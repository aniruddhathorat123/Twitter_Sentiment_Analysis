from textblob import TextBlob
import sys , tweepy
import matplotlib.pyplot as plt

def percentage (part, whole):
    return 100*float(part)/float(whole)


consumerKey = 'tJ0oqPYlQWrbfXGwty619zwdM'
consumerSecret = 'v7bue06QFpUPEtRyBdw86YA5qfCdte6hk9DbkHBFVNLJBTGMe0'
accessToken = '2958139430-xp4nXrgEzeIRadGW5DiknA5YbQdKAwJ4B9xeHyb'
accessTokenSecret = 'hO3L5JZaAiVW5P9rSL9gnaW7z3TggZnDsoPFJYS9iDeLI'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

searchTerm = input("Enter keyword or Item to search:")
noOfSearchTerms = int(input("Enter number of tweets to analyze:"))

tweets = tweepy.Cursor(api.search, q=searchTerm).items(noOfSearchTerms)

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if(analysis.sentiment.polarity == 0):
        neutral +=1

    elif(analysis.sentiment.polarity > 0.00):
        positive += 1

    elif(analysis.sentiment.polarity < 0.00):
        negative += 1


positive = percentage(positive, noOfSearchTerms)
negative = percentage(negative, noOfSearchTerms)
neutral = percentage(neutral, noOfSearchTerms)
polarity = percentage(polarity, noOfSearchTerms)

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')
#polarity = format(polarity, '.2f')

print("Peoples Post on: "+searchTerm+ " By analyzing: "+str(noOfSearchTerms)+" number of tweets.")

if(polarity == 0):
    print("neutral:"+neutral)
elif(polarity < 0.00):
    print("Negative:"+negative)
elif(polarity > 0.00):
    print("Positive:"+positive)


labels = ['Positive['+str(positive)+'%]', 'Negative['+str(negative)+'%]', 'Neutral['+str(neutral)+'%]']
sizes = [positive, negative, neutral]
colors = ['red', 'green', 'blue']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title("Peoples Post on: "+searchTerm+" By analyzing: "+str(noOfSearchTerms)+" number of tweets.")
plt.axis('equal')
plt.tight_layout()
plt.show()
