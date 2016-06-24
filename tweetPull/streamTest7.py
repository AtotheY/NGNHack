from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from sentiment import getSentimentScore
from twitterbot import sendTweet
import json
import MySQLdb
db = MySQLdb.connect(host="localhost", user="root", passwd=".....1",db="tweets")

cur = db.cursor()
#consumer key, consumer secret, access token, access secret.
ckey="e7pFgQ8ttcFhLv9XwkXjxCw5K"
csecret="Q90ORVxhMGpAAqnHQ4MZJnpunfetuPQK9cRmIVirXyUbPqB0rQ"
atoken="746283541105803264-2bPojhnyxArU4HusmNIslbyanUeGkC3"
asecret="UsrMemhlYNAO5DLhM77oXKBTzVs3yTDt3WRZhUOSvWnQA"
class listener(StreamListener):

    def on_data(self, data):
	parsed = json.loads(data)
	Tid = str(parsed['id'])
	tweet = parsed['text']
	keyword = ""
	if "Small business" in text:
		keyword = "Small business"
	else if "Taxes" in text:
		keyword = "Taxes"
	else if "Tax" in text:
		keyword = "Tax"
 	else if business in text:
		keyword = "Business"
	else if "Need accountant" in text:
		keyword = "Need accountant"
	else if "Intuit" in text:
		keyword = "Intuit"
	else if "Financial loss" in text:
		keyword = "Financial loss"
	else if "profit" in text:
		keyword = "profit"
	else if "Cash flow" in text:
		keyword = "Cash flow"
	else if "Entrepreneur" in text:
		keyword = "Entrepreneur"
	else if "Hate accounting" in text:
		keyword = "Hate accounting"
	else if "Find accountant" in text:
		keyword = "Find accountant"
	else if "Accounting hard" in text:
		keyword = "Accounting hard"
	else if "Accounting difficult" in text:
		keyword = "Accounting difficult"
	else if "Save money" in text:
		keyword = "Save money"
	else if "Budget" in text:
		keyword = "Budget"
	else if "Saving" in text:
		keyword = "Saving" 
	location = parsed['user']['location']
	userName = parsed['user']['screen_name']
	created_at = parsed['created_at']
	score = getSentimentScore(tweet)[0]
	print(score)
	if score < -0.60:
        	sendTweet(userName, keyword)
	

	try:
	    cur.execute('''INSERT into tweet2 (tweetid, text, location, date, score, tag) values (%s, %s, %s, %s, %s, %s)''',(Tid, tweet, location, created_at, score, keyword))
	    db.commit()
	except ValueError:
	    print ("ERROR inputting to sql") 
        print(parsed['text'])
	print(Tid)
        return(False)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Financial loss"])
db.close()
