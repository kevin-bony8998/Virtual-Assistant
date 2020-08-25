from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import statistics
#import keras
import numpy as np
import pandas as pd
import tensorflow.keras as keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import tensorflow as tf
import textdistance
import sys
sess = tf.compat.v1.Session()
tf.compat.v1.enable_eager_execution()
print("Wassup?"+str(tf.compat.v1.enable_eager_execution()))
print(tf.executing_eagerly())

@tf.function
def custom_error_finder(y_actual,y_pred):
	with sess.as_default():
		tf.compat.v1.enable_eager_execution()
		global count
		print("Wassup?"+str(tf.compat.v1.enable_eager_execution()))
		print("Bleh"+str(y_actual[0]))
		print(tf.executing_eagerly())
		count = count+1
		print("Count: "+str(count))
		qw = tf.py_function((y_actual).numpy())
		print("Second")
		ya = ((y_actual[0].numpy()).decode())
		yp = ((y_pred[0].numpy()).decode())
		for i,j in ya,yp:
			if i!=j:
				count = count+1
		mse = pow(count,2)/len(ya)
		return mse




count = 0
model = Sequential()
scraper_data = pd.read_csv("C:/Users/KEVINBONYTHEKKANATH-/Desktop/Projects/Chatbot/Combined_new.csv")

scraper_data_columns = scraper_data.columns

predictors = scraper_data["Given"] # We just have the "Given" column as input
target = scraper_data['Target'] # Target column

X_train, X_test, y_train, y_test = train_test_split(predictors, target, test_size=0.01, random_state=42)
n_cols = predictors.shape[0]
print("Shape of predictors is: "+str(predictors.shape))
print("Shape of predictors is (specific): "+str(predictors.shape[0]))

print("Length of y_train",len(y_train))
print("Length of y_test",len(y_test))

print("Length of X_train",len(X_train))
print("Length of X_test",len(X_test))


print("Type of y:",type(y_train))
y_train = y_train.values.tolist()
print("Type of y:",type(y_train))

for i in range(len((y_train))):
	y_train[i] = str(y_train[i])

y_test = y_test.values.tolist()
for i in range(len((y_test))):
	y_test[i] = str(y_test[i])

print("Type of element of y:",type(y_train[0]))
print("Type of element of x:",type(X_train[0]))
#print("Actual element of x:",(X_train[0]))
#print("Actual element of y:",(y_train[0]))
X_train = (tf.constant(X_train).numpy())
X_test = (tf.constant(X_test).numpy())
y_train = (tf.constant(y_train).numpy())
y_test = (tf.constant(y_test).numpy())

print("Type of y_train tensor",y_train.dtype)
print("Type of y_test tensor",y_test.dtype)

model.add(Dense(1, activation = 'relu', input_dim = 1))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(1, activation = 'relu'))

model.compile(optimizer = 'adam',
					run_eagerly=True,
					loss = custom_error_finder)
model.run_eagerly = True
model.fit(X_train, y_train, epochs=200, verbose =1)
predictions = model.predict(X_test)
model.save("Hades.h5")

'''
def custom_error_finder(y_actual,y_pred):
	global row
	row = row+1
	with g.as_default():
		sess = tf.Session()
		count = 0
		a_value=''
		print(y_actual)
		print(y_pred)
		print("Hello")
		#tf.print(y_actual,output_stream=sys.stderr)
		a_trial = K.print_tensor(y_pred, message='y_pred = ')
		tf.print("y_actual: "+str(y_actual.eval(session = sess)))
		tf.print(y_pred)
		#print("Bye")
		#if tf.reduce_all(tf.math.equal(y_pred, y_actual)):
		#	count=count
		#else:
		#	count = count+1
		print("Hello, how do you do?")
		for first,second in tf.unstack(y_actual),tf.unstack(y_pred):
			print("sup")
			print(first,second)
			if first!=second:
				count = count+1
	return int(count)
'''