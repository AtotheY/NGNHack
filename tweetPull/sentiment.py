#Author: Music
import sys
import os
import unirest
import MySQLdb

def getSentimentScore(text):
    sentiment_score = {'Neutral':0, 'pos':1, 'Negative':-1, 'neg':-1, 'Positive':1, 'neutral':0}
    sentiment1, confidence1 = viveknAPI(text)
    score1 = sentiment_score[sentiment1] * float(confidence1) / 100
    #print sentiment1, confidence1, score1
    
    sentiment2, confidence2 = NLTKAPI(text)
    score2 = sentiment_score[sentiment2] * confidence2
    #print sentiment2, confidence2, score2
    return score1, score2
    
def viveknAPI(text):
    response = unirest.post("http://sentiment.vivekn.com/api/text/", headers={"Accept":"application/json"}, params={"txt":text})
    result = response.body['result']
    return (result['sentiment'], result['confidence'])
    #print response.code
    #print response.headers
    #print response.body
    #print response.raw_body

def NLTKAPI(text):
    response = unirest.post("http://text-processing.com/api/sentiment/", headers={"Accept":"application/json"}, params={"text":text})
    ans = response.body
    label = ans['label']
    confidence = ans['probability'][label]
    return label, confidence

if __name__ == "__main__":
    #getSentimentScore('I hate it')
    #score = getSentimentScore("haha")
    db = MySQLdb.connect(host="localhost", user="root", passwd=".....1",db="tweets")
    cursor = db.cursor()
    query = 'select tweetid, text from tweet2 where score is NULL'
    cursor.execute(query)
    for (tweetid, text) in cursor:
        score1, score2 = getSentimentScore(text)
        query = "update tweet2 set score=%s where tweetid=%s"%(score1, tweetid)
        print query
        cursor = db.cursor()
        cursor.execute(query)
        db.commit()
        
