# -*- coding: utf-8 -*-
"""xylemweatherNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PxZCNu6VaSBM4jpWvRdlYoTt1V7wYenv
"""

import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import model_selection
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib as plt
import numpy as np


data = pd.read_csv("/content/yearly_monthly_averages.csv")
data_no_humidity = data.drop(columns="humidity") 
print(data.head())
print(data_no_humidity.head())
corr = data.corr()

col_list = []
for col in data.columns:
  col_list.append(col)
col_tuple = tuple(col_list)

#output data creation
humidity_list = data["humidity"]
print(humidity_list)
humidity_YESNO = []
for x in humidity_list:
  if x > 85:
    humidity_YESNO.append(1)
  else:
    humidity_YESNO.append(0)

#input data creation
input_data = []
for x in range(0, 132):
  x_list = list(data_no_humidity.iloc[x])
  input_data.append(x_list)

X_train, X_test, y_train, y_test = model_selection.train_test_split(data, humidity_list, test_size=0.15, random_state=3)

print(X_train)
print(y_train)

print("These numbers will be seeing how accurate we can predict humidity AS A NUMBER: ")

#neural network
number = 0
acc = 0

for x in range(1, 100):
  nnet = MLPClassifier(hidden_layer_sizes=(x), random_state=1, max_iter=10000000)
  nnet.fit(X_train, list(y_train))
  predictions = nnet.predict(X_test)
  accuracy_value = accuracy_score(y_test, predictions)*100
  if accuracy_value > acc:
    acc = accuracy_value
    number = x

print(number, acc)

number2 = 0
acc2 = 0

#knearestneighbors
for x in range(1, 100):
  knn = KNeighborsClassifier(n_neighbors = x)
  knn.fit(X_train, y_train)
  predictions = knn.predict(X_test)
  accuracy_value = accuracy_score(y_test, predictions)*100
  if accuracy_value > acc2:
    acc2 = accuracy_value
    number2 = x

print(number2, acc2)

print("These numbers will be seeing how accurate we can predict humidity TO SEE IF IT IS GREATER THAN 85: ")

X_train, X_test, y_train, y_test = model_selection.train_test_split(data_no_humidity, humidity_YESNO, test_size=0.15, random_state=3)

#neural network
number3 = 0
acc3 = 0

for x in range(1, 100):
  nnet = MLPClassifier(hidden_layer_sizes=(x), random_state=1, max_iter=10000000)
  nnet.fit(X_train, y_train)
  predictions = nnet.predict(X_test)
  accuracy_value = accuracy_score(y_test, predictions)*100
  if accuracy_value > acc3:
    acc3 = accuracy_value
    number3 = x

print(number3, acc3)

number4 = 0
acc4 = 0

#knearestneighbors
for x in range(1, 100):
  knn = KNeighborsClassifier(n_neighbors = x)
  knn.fit(X_train, y_train)
  predictions = knn.predict(X_test)
  accuracy_value = accuracy_score(y_test, predictions)*100
  if accuracy_value > acc2:
    acc2 = accuracy_value
    number2 = x

print(number2, acc2)

X_train, X_test, y_train, y_test = model_selection.train_test_split(data_no_humidity, humidity_list, test_size=0.15, random_state=3)
model = MLPClassifier(hidden_layer_sizes=(100), solver="lbfgs", random_state=1, max_iter=10000000)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
accuracy = accuracy_score(predictions, y_test)
print(accuracy)

"""Something strange: neither the coefficients NOR the predicted probabilities match the number of parameters there are. Is this specific to MLPClassifier?"""

classes = model.classes_
coeff = model.predict_proba(X_test)
columns = X_test.columns
print(classes)
print(columns)
print(coeff)

coefficients = pd.Series(coeff[0], columns)
print(coefficients)