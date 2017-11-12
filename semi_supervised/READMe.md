# SemiSupervised Approach

We collect the handles of different people belonging to different persona, on basis of of the popularity of the person.

We then crawled tweets made by these handles, using **TwitterSearch** API.

## File Description 
* tfidf.py : generates tfidf vector of all the tweets
* twitter_search.py : crawls the data using twitter api. Obtains tweets created by the handlers pre decided on the basis of their popularity and frequency of tweeting.
* TwitterDataCrawlCode : Directory contains following files :
  * crawlData.py : alternate python code to crawl data using **tweepy** API.
  *most_common_diseases.csv : the csv files of the most_common_diseases
  * patients_keywords.csv :  the csv files containing keywords used by patients.
  * pharmacist_keywords.csv : the csv files containing keywords used by pharmacist .
  
* NN : Directory contains 2 files:
  * d.csv : contains tfidf values of all the tweets we have crawled.
  * personalNN.py : CNN model (deep learning) used for data classification.
