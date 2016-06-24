#Author: Music
import sys
import os
import unirest
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user="root", passwd=".....1",db="tweets")
    cursor = db.cursor()
    query = 'select score, tag from tweet2'
    cursor.execute(query)
    f = open('neil.txt', 'w')
    for (score, tag) in cursor:
        f.write(str(score) +','+tag+'\n')
        print score,tag
        
