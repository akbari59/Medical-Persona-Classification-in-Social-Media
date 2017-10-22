from TwitterSearch import *
import sys,os
m=sys.argv[1]
os.system('mkdir '+'journalist/'+m)
fp=open('key_words','r').readlines()
key_words=[]
for word in fp:
	key_words.append(word[:len(word)-1])
fp1=open('journalist/'+m+'/full_info','w+')
fp2=open('journalist/'+m+'/parsed_info','w+')
fp3=open('journalist/'+m+'/features','w+')
try:
	tso=TwitterSearchOrder()
	tso.set_count(10)
	tso.set_keywords(key_words,or_operator = True)
	tso.add_keyword("from:"+m)
	ts = TwitterSearch(
        consumer_key = 'HoFcB01RSFfjH5JsWLEQSrFoE',
        consumer_secret = 'SUHPOIzgrcvGIVkjwWLrMmUPcyTYlE7QueFfRsRgTQGmsMOaHz',
        access_token = '3195213416-ayJfcbaZ8kF50OflTS4jJKLZ1tkDCqIXWPLZ3Xl',
        access_token_secret = 'mNXaGugwZui9Xc8OT9R6iwzGScRR0nI5hVSCbC4gMEzfv'
     )
	for tweet in ts.search_tweets_iterable(tso):
		print tweet
		fp1.write(str(tweet))
		fp1.write('\n')
		fp2.write(str(tweet['user']['followers_count'])+',_'+str(tweet['user']['friends_count'])+',_'+str(tweet['entities']['user_mentions'])+',_'+str(tweet['retweet_count'])+',_'+str(tweet['entities']['hashtags'])+',_'+str(tweet['entities']['urls']))
		fp2.write("\nTWEET\n")
		fp2.write(tweet['text'].encode('utf-8'))
		fp2.write('\n')
		fp3.write(str(tweet['user']['followers_count'])+',_'+str(tweet['user']['friends_count'])+',_'+str(len(tweet['entities']['user_mentions']))+',_'+str(tweet['retweet_count'])+',_'+str(len(tweet['entities']['hashtags']))+',_'+str(len(tweet['entities']['urls']))+',_'+str(len(tweet['text'].split(' '))))
		fp3.write("\nTWEET\n")
		fp3.write(tweet['text'].encode('utf-8'))
		fp3.write('\n')
		fp1.write('###################\n')
		fp2.write('###################\n')
		fp3.write('###################\n')
except TwitterSearchException as e: 
    print(e)
