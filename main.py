from textblob import TextBlob
from tkinter import *
import sys , tweepy
import matplotlib.pyplot as plt
from tkinter.scrolledtext import ScrolledText


def percentage (part, whole):
    return 100*float(part)/float(whole)

def call_sentiment():
    consumerKey = 'tJ0oqPYlQWrbfXGwty619zwdM'
    consumerSecret = 'v7bue06QFpUPEtRyBdw86YA5qfCdte6hk9DbkHBFVNLJBTGMe0'
    accessToken = '2958139430-xp4nXrgEzeIRadGW5DiknA5YbQdKAwJ4B9xeHyb'
    accessTokenSecret = 'hO3L5JZaAiVW5P9rSL9gnaW7z3TggZnDsoPFJYS9iDeLI'

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth)


    searchTerm = st.get()
    searchTerm = str(searchTerm)
    noOfSearchTerms = nst.get()
    noOfSearchTerms = int(noOfSearchTerms)
    tweets = tweepy.Cursor(api.search, q=searchTerm).items(noOfSearchTerms)

    positive = 0
    negative = 0
    neutral = 0
    polarity = 0
    tw = ""

    for tweet in tweets:
        twets.insert(END, tweet.text+"\n---------\n")
        #tw = tw+tweet.text+"\n"
        analysis = TextBlob(tweet.text)
        polarity += analysis.sentiment.polarity

        if (analysis.sentiment.polarity == 0):
            neutral += 1

        elif (analysis.sentiment.polarity > 0.00):
            positive += 1

        elif (analysis.sentiment.polarity < 0.00):
            negative += 1

    #twets.insert(END, tw)

    positive = percentage(positive, noOfSearchTerms)
    negative = percentage(negative, noOfSearchTerms)
    neutral = percentage(neutral, noOfSearchTerms)
    polarity = percentage(polarity, noOfSearchTerms)

    positive = format(positive, '.2f')
    negative = format(negative, '.2f')
    neutral = format(neutral, '.2f')
    # polarity = format(polarity, '.2f')

    print("Peoples Post on: " + searchTerm + " By analyzing: " + str(noOfSearchTerms) + " number of tweets.")

    if (polarity == 0):
        print("neutral:" + neutral)
    elif (polarity < 0.00):
        print("Negative:" + negative)
    elif (polarity > 0.00):
        print("Positive:" + positive)

    labels = ['Positive[' + str(positive) + '%]', 'Negative[' + str(negative) + '%]', 'Neutral[' + str(neutral) + '%]']
    sizes = [positive, negative, neutral]
    colors = ['red', 'green', 'blue']
    patches, texts = plt.pie(sizes, colors=colors, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.title("Peoples Post on: " + searchTerm + " By analyzing: " + str(noOfSearchTerms) + " number of tweets.")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


root = Tk()
root.title("Twitter Sentiment Analysis")
root.geometry("1000x1000")


st = Entry(root)
nst = Entry(root)
search_lbl = Label(root, text = "Keyword:")
no_twt_lbl = Label(root, text = "number of tweets")
twets = ScrolledText(root, width = 100, height = 100)

bt1 = Button(root, text = "Make Sentiment", command = call_sentiment)

search_lbl.grid(row=0)
st.grid(row=0, column=1)
no_twt_lbl.grid(row=1, column=0)
nst.grid(row=1, column=1)
bt1.grid(row=3, column=1)
twets.grid(row=4 , columnspan = 3)

root.mainloop()
