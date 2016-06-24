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
ckey="KdRTI0oBAIk94w7PiofD0cmo7"
csecret="xIN5Musw80Rlip31To4Gnfx4cZUm2KEoH500hkoLoUL7gmil1y"
atoken="962554652-W3uFUXOMI6UYffcRTConjYBDY3QkcbqH6QBjqE0u"
asecret="DaurNka3j8r9Yc6ALwIxMJdyJZLFGdVhweIRHnosL31Jw"
keyword = "Entrepreneur"
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
	sendTweet(userName, keyword)
	try:
	    cur.execute('''INSERT into tweet2 (tweetid, text, location, date, score, tag) values (%s, %s, %s, %s, %s, %s)''',(Tid, tweet, location, created_at, score, keyword))
	    db.commit()
	except ValueError:
	    print ("ERROR inputting to sql") 
        print(parsed['text'])
	print(Tid)
        return(True)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Entrepreneur"])
db.close()
