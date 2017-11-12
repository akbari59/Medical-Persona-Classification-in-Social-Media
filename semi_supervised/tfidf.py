import os
import numpy as np
import time ,random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.pipeline import FeatureUnion
classes=['caretaker','consultant','journalists','researchers']
other_classes=['patients','pharmacist']
full_data=[]
data=[]
labels=[]
for c in other_classes:
	files=os.listdir(c)
	for f in files:
		print c,f
		fp=open(c+'/'+f,'r').readlines()[1:]
		twt=' '.join(fp[:len(fp)-1])
		twt=twt.replace('\n','')
		twt=twt.replace('Learn more:','')
		tep=twt.split(' ')
		for j in range(0,len(tep)):
			if 'http' in tep[j]:
				tep[j]=''
		twt=' '.join(tep)
		feature=fp[len(fp)-1]
		feature=feature.split(',_')
		feature=np.asarray(feature).astype(int)
		full_data.append((feature,twt,c))
		print twt,feature
		# break



for c in classes:
	directories=os.listdir(c)
	for d in directories:
		print c,d
		fp=open(c+'/'+d+'/features','r').readlines()
		for i in range(0,len(fp)):
			fp[i]=fp[i].replace('\n','')
		temp=' '.join(fp)
		tweets=temp.split('###################')
		for tweet in tweets:
			if tweet!='':
				feature=tweet.split('TWEET')[0]
				twt=tweet.split('TWEET')[1]
				twt=twt.replace('Learn more:','')
				tep=twt.split(' ')
				for j in range(0,len(tep)):
					if 'http' in tep[j]:
						tep[j]=''
				twt=' '.join(tep)
				feature=feature.split(',_')
				feature=np.asarray(feature).astype(int)
				full_data.append((feature,twt,c))
				data.append(twt)
				labels.append(c)
				print feature,twt
		# break

L=len(full_data)
random.shuffle(full_data)
train_data=[i[1] for i in full_data[:int(0.8*L)]]
train_features=[i[0] for i in full_data[:int(0.8*L)]]
train_labels=[i[2] for i in full_data[:int(0.8*L)]]
test_data=[i[1] for i in full_data[int(0.8*L):]]
test_features=[i[0] for i in full_data[int(0.8*L):]]
test_labels=[i[2] for i in full_data[int(0.8*L):]]
vectorizer = TfidfVectorizer(min_df=5,max_df = 0.8,sublinear_tf=True,use_idf=True,decode_error='ignore')

train_vectors=vectorizer.fit_transform(train_data)
test_vectors=vectorizer.transform(test_data)
final_train=np.hstack([train_features,train_vectors.toarray()])
final_test=np.hstack([test_features,test_vectors.toarray()])
print final_train

# classifier_rbf = svm.SVC(kernel='rbf')
# classifier_rbf.fit(final_train,train_labels)
# prediction_rbf=classifier_rbf.predict(final_test)
# print(classification_report(test_labels, prediction_rbf))
# print(accuracy_score(test_labels, prediction_rbf))
