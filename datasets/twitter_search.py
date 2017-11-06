from TwitterSearch import *
import sys,os
from collections import defaultdict
from get_time_diff import timediff
from get_smiley import happy , sad
from linguistic_features import feature_getter,pos_getter,get_wotscore , num_stop_words ,num_punc


sl=defaultdict(int)
for i in open("list_swear",'r').readlines():
	i=i.strip().lower()
	sl[i]=1

pos_e=defaultdict(int)
for i in open("postive_emotion",'r').readlines():
	i=i.strip().lower()
	pos_e[i]=1

neg_e=defaultdict(int)
for i in open("negative_emotion",'r').readlines():
	i=i.strip().lower()
	neg_e[i]=1

def pos_emo(text):
	words=text.split(" ")
	sc=0
	for word in words:
		if word.lower() in pos_e:
			sc+=1
			break
	return sc

def neg_emo(text):
	words=text.split(" ")
	sc=0
	for word in words:
		if word.lower() in neg_e:
			sc+=1
			break
	return sc


def swear_number(text):
	words=text.split(" ")
	sc=0
	for word in words:
		if word.lower() in sl:
			sc=1
			break
	return sc

def get_features(tweet):
	features=[]
	features.append(timediff(tweet['created_at']))
	if('web' in tweet['source']):
		features.append(2)
	elif('mobile' in tweet['source']):
		features.append(1)
	else:
		features.append(0)
	if(tweet['coordinates']==None):
		features.append(0)
		features.append(0)
	else:
		a,b=tweet['coordinates']
		features.append(a)
		features.append(b)
	features.append(len(str(tweet['text'].encode('utf-8'))))
	features.append(len(str(tweet['text'].encode('utf-8')).split(" ")))
	features.append(len(tweet['entities']['hashtags']))
	features.append(len(set(str(tweet['text'].encode('utf-8')))))
	features.append(len(tweet['entities']['symbols']))
	features.append(len(tweet['entities']['urls']))
	features.append(happy(str(tweet['text'].encode('utf-8'))))
	features.append(sad(str(tweet['text'].encode('utf-8'))))
	if(":" in str(tweet['text'].encode('utf-8')) or ";" in str(tweet['text'].encode('utf-8'))):
		features.append(1)
	else:
		features.append(0)
	features.append(swear_number(str(tweet['text'].encode('utf-8'))))
	features.append(pos_emo(str(tweet['text'].encode('utf-8'))))
	features.append(neg_emo(str(tweet['text'].encode('utf-8'))))
	features=features+feature_getter(str(tweet['text'].encode('utf-8')))
	features=features+pos_getter(str(tweet['text'].encode('utf-8')))
	features.append(tweet['user']['followers_count'])
	features.append(tweet['user']['friends_count'])
	features.append(timediff(tweet['user']['created_at']))
	features.append(tweet['retweet_count'])
	features.append(len(tweet['entities']['user_mentions']))
	if(tweet['in_reply_to_status_id_str']!=None):
		features.append(1)
	else:
		features.append(0)
	if tweet['retweeted']:
		features.append(1)
	else:
		features.append(0)
	wot=0.0
	for url in tweet['entities']['urls']:
		wot+=get_wotscore(str(url))
	if(wot==0):
		features.append(wot)
	else:
		features.append(wot/len(tweet['entities']['urls']))
	classifier=raw_input("enter pos or neg or neu:")
	if '1' in classifier:
		features.append(1)
	elif '2' in classifier:
		features.append(2)
	elif '3' in classifier:
		features.append(3)
	features.append(num_stop_words(str(tweet['text'].encode('utf-8'))))
	features.append(num_punc(str(tweet['text'].encode('utf-8'))))
	return features


fp=open("drug_list",'r')
for i in fp:
	i=i.strip()
	print i
	try:
		tso=TwitterSearchOrder()
		tso.set_keywords([i])
		tso.set_language('en')
		#tso.add_keyword("from:"+m)
		ts = TwitterSearch(
    	    consumer_key = 'kvNIyBZq0lCdZlRcplINHBlMP',
    	    consumer_secret = '9fFI6t6lcVXYVZxaXlML0zgJsupBgkJQWkXxAgjz65cbYz1iEh',
    	    access_token = '920674452374822912-vpeBh4pCS2DcNQYpwt7S3dkYhe7nm4E',
    	    access_token_secret = 'cQgYn2Z7PReG7KfjkTTu2ca88NRFd3imTdcSqZT8SWsuI'
    	 )

		for tweet in ts.search_tweets_iterable(tso):
			print 'hi'
			print str(tweet['text'].encode('utf-8'))
			features=get_features(tweet)
			category=raw_input("enter category:")
			if('0' in category):
				continue
			if('1' in category):
				fp1=open("caretaker/"+tweet['id_str'],'w')
				features1=[str(i) for i in features]
				strg=','.join(features1)
				fp1.write(strg)
				fp1.write('\n')
				fp1.write(str(tweet['text'].encode('utf-8')))
				fp1.write('\n')
				fp1.write('#############')
				fp1.write('\n')

			if('2' in category):
				fp2=open("consultant/"+tweet['id_str'],'w')
				features1=[str(i) for i in features]
				strg=','.join(features1)
				fp2.write(strg)
				fp2.write('\n')
				fp2.write(str(tweet['text'].encode('utf-8')))
				fp2.write('\n')
				fp2.write('#############')
				fp2.write('\n')
				
			if('3' in category):
				fp3=open("journalists/"+tweet['id_str'],'w')
				features1=[str(i) for i in features]
				strg=','.join(features1)
				fp3.write(strg)
				fp3.write('\n')
				fp3.write(str(tweet['text'].encode('utf-8')))
				fp3.write('\n')
				fp3.write('#############')
				fp3.write('\n')
				
			if('4' in category):
				fp4=open("researcher/"+tweet['id_str'],'w')
				features1=[str(i) for i in features]
				strg=','.join(features1)
				fp4.write(strg)
				fp4.write('\n')
				fp4.write(str(tweet['text'].encode('utf-8')))
				fp4.write('\n')
				fp4.write('#############')
				fp4.write('\n')
				
			if('5' in category):
				fp5=open("patients/"+tweet['id_str'],'w')
				features1=[str(i) for i in features]
				strg=','.join(features1)
				fp5.write(strg)
				fp5.write('\n')
				fp5.write(str(tweet['text'].encode('utf-8')))
				fp5.write('\n')
				fp5.write('#############')
				fp5.write('\n')
				
			if('6' in category):
				fp6=open("pharmacist/"+tweet['id_str'],'w')
				features1=[str(i) for i in features]
				strg=','.join(features1)
				fp6.write(strg)
				fp6.write('\n')
				fp6.write(str(tweet['text'].encode('utf-8')))
				fp6.write('\n')
				fp6.write('#############')
				fp6.write('\n')
				
			if('7' in category):
				fp7=open("other/"+tweet['id_str'],'w')
				features1=[str(i) for i in features]
				strg=','.join(features1)
				fp7.write(strg)
				fp7.write('\n')
				fp7.write(str(tweet['text'].encode('utf-8')))
				fp7.write('\n')
				fp7.write('#############')
				fp7.write('\n')
				
	except TwitterSearchException as e: 
	    print(e)
