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
keyword = "Small business"
class listener(StreamListener):
    def on_data(self, data):
	parsed = json.loads(data)
	Tid = str(parsed['id'])
	tweet = parsed['text']
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
	return False

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Small business"])
db.close()
