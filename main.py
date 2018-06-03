from textblob import TextBlob
from tkinter import *
import sys , tweepy
import matplotlib.pyplot as plt
from tkinter.scrolledtext import ScrolledText


def percentage (part, whole):
    return 100*float(part)/float(whole)

def call_sentiment():
    

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
    tw=""
    r = 7


    for tweet in tweets:
        tweet_text = tweet.text
        char_list = [tweet_text[j] for j in range(len(tweet_text)) if ord(tweet_text[j]) in range(65536)]
        tweet_t = ''
        for j in char_list:
            tweet_t = tweet_t + j
        analysis = TextBlob(tweet.text)
        polarity += analysis.sentiment.polarity

        twets = ScrolledText(root, width=80, height=5)
        tid = ScrolledText(root, width=20, height=5)
        pola = ScrolledText(root, width=20, height=5)
        result = ScrolledText(root, width=20, height=5)

        tid.grid(row=r)
        twets.grid(row=r, column=1)
        pola.grid(row=r, column=2)
        result.grid(row=r, column=3)
        r=r+1


        if (analysis.sentiment.polarity == 0):
            neutral += 1
            tid.insert(END, tweet.id)
            twets.insert(END, tweet_t)
            pola.insert(END, analysis.sentiment.polarity)
            result.insert(END, "Neutral")


        elif (analysis.sentiment.polarity > 0.00):
            positive += 1
            tid.insert(END, tweet.id)
            twets.insert(END, tweet_t)
            pola.insert(END, analysis.sentiment.polarity)
            result.insert(END, "Positive")

        elif (analysis.sentiment.polarity < 0.00):
            negative += 1
            tid.insert(END, tweet.id)
            twets.insert(END, tweet_t)
            pola.insert(END, analysis.sentiment.polarity)
            result.insert(END, "Negative")

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
root.geometry("1500x1000")



st = Entry(root)
nst = Entry(root)
search_lbl = Label(root, text = "Keyword:")
no_twt_lbl = Label(root, text = "number of tweets")

bt1 = Button(root, text = "Make Sentiment", command = call_sentiment)
lbl_uname = Label(root, text = "Username")
lbl_tweet = Label(root, text = "Tweet")
lbl_polarity = Label(root, text = "Polarity")
lbl_result = Label(root, text = "Result")


search_lbl.grid(row=0,column = 1)
st.grid(row=0, column=2)
no_twt_lbl.grid(row=1, column=1)
nst.grid(row=1, column=2)
bt1.grid(row=3, column=2)
lbl_uname.grid(row=5)
lbl_tweet.grid(row=5,column=1)
lbl_polarity.grid(row=5,column = 2)
lbl_result.grid(row=5, column= 3)


root.mainloop()
