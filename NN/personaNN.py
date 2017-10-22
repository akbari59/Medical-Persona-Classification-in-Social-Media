import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder
import numpy
numpy.random.seed(7)

dataframe = pandas.read_csv("d.csv", header=None)
dataset = dataframe.values
X = dataset[:,0:-1].astype(float)
Y = dataset[:,-1]

encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
dummy_y = np_utils.to_categorical(encoded_Y)

model = Sequential()
model.add(Dense(400, input_dim=282, activation='relu'))
model.add(Dense(300, activation='relu'))
model.add(Dense(6, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, dummy_y, epochs=150, batch_size=10)

scores = model.evaluate(X, dummy_y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))