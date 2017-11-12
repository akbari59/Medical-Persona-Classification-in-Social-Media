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



from keras.callbacks import Callback
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score

def f1(y_true,y_pred):
	print y_true,y_pred
	c1 = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
	c2 = K.sum(K.round(K.clip(y_pred, 0, 1)))
	c3 = K.sum(K.round(K.clip(y_true, 0, 1)))
	if c3 == 0:
		return
	precision = c1 / c2
	recall = c1 / c3
	f1_s = 2 * (precision * recall) / (precision + recall)
	return recall


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



file_labels=defaultdict(list)
directories=[x[1] for x in os.walk('./')][0][:-1]
data=[]
for i in directories:
	files=os.listdir(i)
	for j in files:
		file_labels[j].append(i)
		features=open(i+'/'+j,'r').readlines()[0].split(',')
		text_gen=open(i+'/'+j,'r').readlines()[1:-1]
		text_gen='\n'.join(text_gen)
		data.append((features,text_gen,list(set(file_labels[j])),i,j))
F_train=[]
random.shuffle(data)
train_data=[]
train_labels=[]
for c in data:
	F_train.append([float(i.strip()) for i in c[0]])
	train_data.append(c[1])
	train_labels.append(c[2])

for i in range(0,len(F_train)):
	try:
		F_train[i]=np.asarray(F_train[i][13:28]+F_train[i][37:39])
	except:
		print F_train[i]

F_train=np.asarray(F_train)

vocabulory=np.unique(np.hstack(train_data))
X_train=[]

for i in train_data:
	X_train.append(text.one_hot(i,len(vocabulory)))

X_train = sequence.pad_sequences(X_train, maxlen=250)

encoder=MultiLabelBinarizer(classes=directories)
encoder.fit(directories)
y_train=encoder.transform(train_labels)
L=len(X_train)
X_test=X_train[:int(0.8*L)]
y_test=y_train[:int(0.8*L)]

# model = Sequential()
# model.add(Embedding(len(vocabulory), 32, input_length=250))
# model.add(Conv1D(filters=32, kernel_size=3, padding='same', activation='relu'))
# model.add(MaxPooling1D(pool_size=2))
# model.add(Flatten())
# model.add(Dense(250, activation='relu'))
# model.add(Dense(7, activation='softmax'))
# model.compile(loss='binary_crossentropy',optimizer='adam', metrics=['accuracy',f1score])
# model.fit(X_train, y_train,validation_split=0.2, epochs=60, batch_size=128, verbose=2)

inputt=Input(shape=(250,))
embedding=Embedding(len(vocabulory), 32, input_length=250)(inputt)
conv=Conv1D(filters=32, kernel_size=3, padding='same', activation='relu')(embedding)
pol=MaxPooling1D(pool_size=2)(conv)
lst=LSTM(196,dropout_U=0.2, dropout_W=0.2)(pol)
seq_features=Dense(250, activation='relu')(lst)
# seq_features=Flatten()(den)

nb_features=len(F_train[0])
other_features=Input(shape=(nb_features,))

model_final=  merge([seq_features , other_features], mode='concat')
#model_final = Dense(250, activation='relu')(model_final)
model_final = Dense(7, activation='softmax')(model_final)
model_final = Model([inputt, other_features], model_final)

model_final.compile(loss='binary_crossentropy',optimizer='adam', metrics=['accuracy',f1score])

model_final.fit([X_train,F_train], y_train,validation_split=0.2, epochs=2, batch_size=128, verbose=2)
