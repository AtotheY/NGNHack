import tweepy

CONSUMER_KEY ="Y4TcZkNeH20IAMpi5MWhHbqdY"
CONSUMER_SECRET = "juuVaNCL49x4h2d2w7M2ZwLXyXrpeKqKs0AyD4ZAvqNkfj0sAo"   
ACCESS_KEY = "746213010713174016-Q2x9zXrUSHGXTfkyACLTo9qXeHFGFnS"    
ACCESS_SECRET = "EisD5hMrtfyM6H4m8HhPPlbeXeRV5UWkS9hpKVoEUUE0p"
mymap = {}
mymap['Small business'] = "Managing a small business can be hard. Let us, at Intuit help you! Try Quickbooks https://quickbooks.intuit.com/"

def sendTweet(user, tag)
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	api.update_status("@"+user + " " + mymap[tag])

