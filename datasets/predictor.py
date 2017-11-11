import sys,os,re
from collections import defaultdict
from get_time_diff import timediff
from get_smiley import happy , sad
from linguistic_features import feature_getter,pos_getter,get_wotscore , num_stop_words ,num_punc

import os,sys,time,csv,random
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.pipeline import FeatureUnion
from collections import defaultdict

from keras.models import Sequential
from keras.layers import Input,Dense,merge, LSTM
from keras.layers import Flatten
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.preprocessing import text
import keras
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder,MultiLabelBinarizer
import keras.backend as K
from keras.models import Model
from keras.models import load_model

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
			sc=1
	return sc

def neg_emo(text):
	words=text.split(" ")
	sc=0
	for word in words:
		if word.lower() in neg_e:
			sc=1
	return sc


def swear_number(text):
	words=text.split(" ")
	sc=0
	for word in words:
		if word.lower() in sl:
			sc=1
	return sc


def get_features(tweet):
	features=[]
	features.append(len(str(tweet)))
	features.append(len(str(tweet).split(" ")))
	features.append(len(set(str(tweet))))
	features.append(happy(str(tweet)))
	features.append(sad(str(tweet)))
	features.append(swear_number(str(tweet)))
	features.append(pos_emo(str(tweet)))
	features.append(neg_emo(str(tweet)))
	features=features+feature_getter(str(tweet))
	features=features+pos_getter(str(tweet))
	features.append(num_stop_words(str(tweet)))
	features.append(num_punc(str(tweet)))
	return features

def f1score(y_true, y_pred, threshold_shift=0.5):
    beta = 2

    # just in case of hipster activation at the final layer
    y_pred = K.clip(y_pred, 0, 1)

    # shifting the prediction threshold from .5 if needed
    y_pred_bin = K.round(y_pred + threshold_shift)

    tp = K.sum(K.round(y_true * y_pred_bin), axis=1) + K.epsilon()
    fp = K.sum(K.round(K.clip(y_pred_bin - y_true, 0, 1)), axis=1)
    fn = K.sum(K.round(K.clip(y_true - y_pred, 0, 1)), axis=1)

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)

    beta_squared = beta ** 2
    return K.mean((beta_squared + 1) * (precision * recall) / (beta_squared * precision + recall + K.epsilon()))


directories=[x[1] for x in os.walk('./')][0]
directories.remove('.ipynb_checkpoints')

while True:
	tweet=raw_input("Enter tweet to be predicted: ")
	words=tweet.split()
	for i in range(0,len(words)):
		if("http" in words[i]):
			words[i]=''
		else:
			words[i]=words[i].lower()
	k=' '.join(words)
	k=re.sub(r'[^\x00-\x7F]+',' ', k)
	features=np.asarray(get_features(k)).reshape(1,23)
	X_test=[]
	X_test.append(text.one_hot(k,1162))
	X_test = sequence.pad_sequences(X_test, maxlen=250)

	model = load_model('final_model.h5')
	predicted=model.predict([X_test,features])
	label=np.argmax(predicted)
	print directories[label]
