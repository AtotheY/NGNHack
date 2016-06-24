import tweepy

CONSUMER_KEY ="e7pFgQ8ttcFhLv9XwkXjxCw5K"
CONSUMER_SECRET = "Q90ORVxhMGpAAqnHQ4MZJnpunfetuPQK9cRmIVirXyUbPqB0rQ"   
ACCESS_KEY = "746283541105803264-2bPojhnyxArU4HusmNIslbyanUeGkC3"    
ACCESS_SECRET = "UsrMemhlYNAO5DLhM77oXKBTzVs3yTDt3WRZhUOSvWnQA"
mymap = {}
mymap['Small business'] = "Managing a small sized business can be hard. Let us, at Intuit help you! Try Quickbooks https://quickbooks.intuit.com/"
mymap['Taxes'] = "Missed the deadline? You can still file and get your maximum refund. Join for free at https://turbotax.intuit.com"
mymap['Tax'] = "Missed the deadline? You can still file and get your maximum refund. Join for free at https://turbotax.intuit.com"
mymap['Business'] = "Love managing your company but hate managing the books? Try Quickbooks https://quickbooks.intuit.com/"
mymap['Need accountant'] = "We would love to connect you with a professional to help"
mymap['Intuit'] = "Join us at http://www.intuit.com to learn how we can help you!" 
mymap['Financial loss'] = "Think you might benefit from a professional accountants support for your company? http://www.intuit.com"
mymap['profit'] = "We think you might do even better next quarter with professional accounting support for your company http://www.intuit.com"
mymap['Cash flow'] = "Need help managing your cash flow? Try Quickbooks https://quickbooks.intuit.com/ and let us know what you think"
mymap['Entrepreneur'] = "You are a champion! But even the best need help with managing their finances. Turbotax and Quickbooks are the prefect products for you."
mymap['Hate accounting'] = "Yes, we understand that it can be really hard. But we are here to help. Try Quickbooks for free and let us know what you think."
mymap['Find accountant'] = "Let us help you find the right accountant for your business."
mymap['Accounting hard'] = "So easy, QuickBooks customers save an average of 11 hours a month"
mymap['Accounting difficult'] = "So easy, QuickBooks customers save an average of 11 hours a month"
mymap['Save money'] = "Effortlessly create budgets that are easy to stick to. We even make a few for you at mint.com"
mymap['Budget'] = "From money and budgeting to customized tips and more, get a clear view of your total financial life."
mymap['Saving'] = "Quickbooks users find an average of $3,809 in potential tax savings per year "
def sendTweet(user, tag):
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	api.update_status("@"+user + " " + mymap[tag])

