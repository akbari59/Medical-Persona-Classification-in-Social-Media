#Created by Sanket Shah
#Date : 16th October, 2017
#Python code to crawl Twitter data using keywords

import tweepy
from tweepy import OAuthHandler
import pandas as pd
from tweepy.streaming import StreamListener
from tweepy import Stream
import json

 
consumer_key = 'OYgHCmh8fkfbUEnEFylgRWLmh'
consumer_secret = '1iZJIWdADMjPUyppLMqPJH2iV3ZDDlfZ8S6YBmFGNYmW9Nn61T'
access_token = '3195213416-vcOOcQtvE0ZV42lh0sHQbjgZjhdq6soyn2F0kqg'
access_token_secret = 'efIcUT4L8pL4wzqYShwddNu5zjdWJzVJ6L6k9Kl7Y5Qww'

data_extraction_keywords=[]

#class to crawl twitter data in a stream
class StdOutListener(StreamListener):

    def on_data(self, data):
        tweet = json.loads(data)
        try:
        	#you can redirect the ouput of this program to a file. 
        	print str(tweet['id'])+","+tweet['user']['name']+","+tweet['user']['screen_name']+","+str(tweet['user']['followers_count'])+","+tweet['text']+","+tweet['user']['description']+","+str(tweet['user']['statuses_count'])
        except:
        	x=1
        return True

    def on_error(self, status):
        print status



f = open('top_50_diseases.csv') #I have taken only diseases into consideration, but we can take other keywords. 

if __name__ == '__main__':

	#to append the data from the file to the list data_extraction_keywords
	for line in f:
		data_extraction_keywords.append(line[:-1])
	#print data_extraction_keywords
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)
	stream.filter(track=data_extraction_keywords) #search for all the tweets which contain one or more keywords.