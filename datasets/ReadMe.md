# This Folder contains the code to extract features from the tweets

### The Features that are extracted from the Tweet MetaData
* Number of seconds since tweet
* Source of tweet
* Geographic Coordinates latitude
* Geographic Coordinates longitude

### The Features that are extracted from Tweet Content
* Number of characters
* Number of words
* Number of URLs
* Number of Hashtags
* Number of unique characters
* Presence of stock symbol
* Presence of happy smiley
* Presence of sad smiley
* Presence of colon

### The Features that are extracted from Tweet Liguistic Content
* Presence of Swear word
* Presence of negative emotion words
* Presence of positive emotion words
* Number of strong subjective adjectives
* Number of weak subjective adjectives
* Number of strong subjective nouns
* Number of weak subjective nouns
* Number of pronouns
* Number of self words
* Number of interjections
* Number of Quantifiers
* Number of wh-words
* Number of modal verbs
* Number of positive adjectives
* Number of negative adjectives
* Number of superlative words
* Number of stop words
* Number of punctuations
* Sentiment of tweet

### The Features that are extracted from Tweet Author
* Number of followers
* Number of friends
* Time since user is on twitter

### The Features that are extracted from Tweet Network
* Number of retweets
* Number of user mentions
* Is tweet a reply
* Number of replies
* Is tweet a retweet

### The Features that are extracted from Tweet Links
* WOT score of URL

### The following files are present in the folder
* twitter_search.py - This is a main python which crawls the tweets using keywords from the drug_list file and uses all the other text and python files to extract features from the crawled data. 
* drug_list - This file contains 441 drugs names which are used for querying twitter data. 
* dynamic.txt - This file contains all those words which describe one's personality. 
* get_smiley.py - This is a python file which is used to fetch all the smileys present in the tweet. The file contains two functions namely happy and sad for detecing happy and sad smiley respectively. 
* get_time_diff.py - This file is used to get the total number of seconds before which the tweet was posted. The reference time taken is Sat Nov 04 14:23:30 +0000 2017. 
* gradable-neg.txt - This file contains all the negative adjectives which can be graded as per the situation. Eg. cold, hot, frightened. You can be cold, or hot(more frightened) or frightened as per the situation. 
* gradable-pos.txt - This file contains all the positive adjectives which can be graded as per the situation. Eg. cold, hot, frightened. You can be cold, or hot(more frightened) or frightened as per the situation. 
* linguistic_features.py - This is python file which is used to get linguistic features like 
	* strong subject adjectives
	* week subject adjectives
	* strong subject nouns
	* weak subject nouns
	* self words
	* polar positive words
	* polar negative words
* list_swear - This file contains the list of words which are slang / abusive.
* negative_emotion - This file contains all the words which describe the negative emotion of a person. 
* polar-neg.txt - This file contains all the words which describe extreme behaviour of a person in a negative sense.
* polar-pos.txt - This file contains all the words which describe extreme behaviour of a person in a positive sense.
* positive_emotion - This file contains all the words which describe the positive emotion of a person.
* self_words - This file contains all the words which are pertaining to one-self. These mainly describe first person speech. 
* strongsubj-adj.txt - This file contains all the words which are positive adjectives describing the subject of the sentence. 
* weaksubj-adj.txt - This file contains all the words which are negative adjectives describing the subject of the sentence. 
* strongsubj-noun.txt - This file contains all the positive nouns in the sentence.
* weaksubj-noun.txt - This file contains all the positive nouns in the sentence.
* superlative_list - This file contains all the words which are having superlative degree. ex. greatest, fastest, etc.