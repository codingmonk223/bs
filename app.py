#Twitter Sentiment Analysis
import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 
from textblob.sentiments import NaiveBayesAnalyzer

from flask import Flask, render_template , redirect, url_for, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def home():
  return render_template("index 1.html")

# ******Phrase level sentiment analysis
@app.route("/predict", methods=['POST','GET'])
def pred():
	if request.method=='POST':
            query=request.form['query']
            count=request.form['num']
            fetched_tweets = get_tweets(api,query, count) 
            return render_template('result.html', result=fetched_tweets)


@app.route("/predict1", methods=['POST','GET'])
def pred1():
	if request.method=='POST':
            text = request.form['txt']
            blob = TextBlob(text)
            if blob.sentiment.polarity > 0:
                text_sentiment = "positive"
            elif blob.sentiment.polarity == 0:
                text_sentiment = "neutral"
            else:
                text_sentiment = "negative"
            return render_template('result1.html',msg=text, result=text_sentiment)


if __name__ == '__main__':
    
    consumer_key = 'M20wUoXj62YVtzCbOEkHB71SX' 
    consumer_secret = '7732TqF7tRC2V3PV9zFEHdak2S9f3Avd95c2xQFu5L2B0EtzDO'
    access_token = '1599298879605772288-gs47KZaxwyzlGdcMKbsMD239QE0MSA'
    access_token_secret = 'qgPDquqDjvtzSoe6AY7hx00t95XxRiRstjEzxFawVpxtn'

    try: 
        auth = OAuthHandler(consumer_key, consumer_secret)  
        auth.set_access_token(access_token, access_token_secret) 
        api = tweepy.API(auth)
    except: 
        print("Error: Authentication Failed") 

    app.debug=True
    app.run(host='localhost')

