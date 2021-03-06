import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import pandas as pd
df=pd.read_csv("sonar.csv",header=None)
x = df.iloc[:,:-1]
y= df.iloc[:,-1]
y=pd.get_dummies(y)
print y
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.20)
model = Sequential()
model.add(Dense(10, input_shape=(60,), activation='relu', name='fc1'))
model.add(Dense(10, activation='relu', name='fc2'))
model.add(Dense(2, activation='softmax', name='output'))
optimizer = Adam(lr=0.001)
model.compile(optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
print('Neural Network Model Summary: ')
print(model.summary())
model.fit(train_x, train_y, verbose=2, batch_size=5, epochs=200)
results = model.evaluate(test_x, test_y)
print('Final test set loss: {:4f}'.format(results[0]))
print('Final test set accuracy: {:4f}'.format(results[1]))
