from TwitterSearch import *
import sys,os
m=sys.argv[1]
os.system('mkdir '+'caretaker/'+m)
fp=open('key_words','r').readlines()
key_words=[]
for word in fp:
	key_words.append(word[:len(word)-1])
fp1=open('caretaker/'+m+'/full_info','w+')
fp2=open('caretaker/'+m+'/parsed_info','w+')
fp3=open('caretaker/'+m+'/features','w+')
try:
	tso=TwitterSearchOrder()
	tso.set_count(100)
	tso.set_keywords(key_words,or_operator = True)
	tso.add_keyword("from:"+m)
	ts = TwitterSearch(
        consumer_key = 'Dtvh3omh0KWl57nr2HQyUh59y',
        consumer_secret = 'IfLVLuB9vjYRWLl5wAuJeDVCzLDKKpULfndqsfljYZh7h1tC3c',
        access_token = '920674452374822912-SflTtjg4BgZRvcgvVVrdecMdS6qoomV',
        access_token_secret = 'Sz7Yi4uKnqf2dgWtjzJgUQBZur2ixIY7kcxmj4DeLcr3g'
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