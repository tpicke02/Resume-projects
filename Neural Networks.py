# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 09:29:19 2019

@author: Thomas Pickering
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.metrics import mean_squared_error

#Auto
auto_headers = ["target", "cyl", "disp", "hp", "wt", "accel", "year", "origin", "car_name"]
auto = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data", 
                   sep = "\s+", names = auto_headers, na_values = "?")
auto.dropna(inplace=True)
auto["car_name"] = auto["car_name"].astype('category')
auto["car_name_cat"] = auto["car_name"].cat.codes
auto.head()
del auto['car_name']

x = auto.drop('target', axis=1)
y = auto['target']
x_train, x_test, y_train, y_test = train_test_split(x, y)

scaler = StandardScaler()
scaler.fit(x_train)
x_train_scale = scaler.transform(x_train)
x_test_scale = scaler.transform(x_test)
    
regr = MLPRegressor() 
regr.fit(x_train_scale, y_train)
predictions = regr.predict(x_test_scale)
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error: {}".format(mse)) 
    

#Wine Data
wine = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",
    names = ["Cultivator", "Alchol", "Malic_Acid", "Ash", "Alcalinity_of_Ash",
             "Magnesium", "Total_phenols", "Falvanoids", "Nonflavanoid_phenols", 
             "Proanthocyanins", "Color_intensity", "Hue", "OD280", "Proline"])
x2 = wine.drop('Cultivator',axis=1)
y2 = wine['Cultivator']
x_train2, x_test2, y_train2, y_test2 = train_test_split(x2, y2)

scaler.fit(x_train2)
x_train2 = scaler.transform(x_train2)
x_test2 = scaler.transform(x_test2)

mlp2 = MLPClassifier()
mlp2.fit(x_train2,y_train2)
predictions_wine = mlp2.predict(x_test2)

accuracy2 = accuracy_score(y_test2, predictions_wine)
print("Wine Accuracy: {}".format(accuracy2))
print(classification_report(y_test2, predictions_wine))

#Census Income
income_headers = ["age", "workclass", "flnwgt", "education", "education-num",
                  "marital-status", "occupation", "relationship", "race", "sex",
                  "capital-gain", "capital-loss", "hours-per-week", 
                  "native-country", "income_target"]
income = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",
                     names = income_headers)

income['workclass'].value_counts()
income["workclass"] = income["workclass"].astype('category')
income["workclass_cat"] = income["workclass"].cat.codes

income['education'].value_counts()
income["education"] = income["education"].astype('category')
income["education_cat"] = income["education"].cat.codes

income['marital-status'].value_counts()
income["marital-status"] = income["marital-status"].astype('category')
income["marital-status_cat"] = income["marital-status"].cat.codes

income['occupation'].value_counts()
income["occupation"] = income["occupation"].astype('category')
income["occupation_cat"] = income["occupation"].cat.codes

income['relationship'].value_counts()
income["relationship"] = income["relationship"].astype('category')
income["relationship_cat"] = income["relationship"].cat.codes

income['race'].value_counts()
income["race"] = income["race"].astype('category')
income["race_cat"] = income["race"].cat.codes

income['sex'].value_counts()
income["sex"] = income["sex"].astype('category')
income["sex_cat"] = income["sex"].cat.codes

income['native-country'].value_counts()
income["native-country"] = income["native-country"].astype('category')
income["native-country_cat"] = income["native-country"].cat.codes

income['income_target'].value_counts()
income["income_target"] = income["income_target"].astype('category')
income["income_target_cat"] = income["income_target"].cat.codes

income = income.drop(columns=["workclass", "education", "marital-status", "occupation",
   "relationship", "race", "sex", "native-country", "income_target"])

x3 = income.drop("income_target_cat",axis=1)
y3 = income["income_target_cat"]
x_train3, x_test3, y_train3, y_test3 = train_test_split(x3, y3)

scaler.fit(x_train3)
x_train3 = scaler.transform(x_train3)
x_test3 = scaler.transform(x_test3)

mlp3 = MLPClassifier()
mlp3.fit(x_train3,y_train3)
predictions_income = mlp3.predict(x_test3)

accuracy3 = accuracy_score(y_test3, predictions_income)
print("Income Accuracy: {}".format(accuracy3))
print(classification_report(y_test3, predictions_income))

#Poker Stats
poker = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-training-true.data")
x4 = poker.drop("9",axis=1)
y4 = poker["9"]
x_train4, x_test4, y_train4, y_test4 = train_test_split(x4, y4)

scaler.fit(x_train4)
x_train4 = scaler.transform(x_train4)
x_test4 = scaler.transform(x_test4)

mlp4 = MLPClassifier(hidden_layer_sizes=(13,13,13), max_iter=500)
mlp4.fit(x_train4,y_train4)
predictions_poker = mlp4.predict(x_test4)

accuracy4 = accuracy_score(y_test4, predictions_poker)
print("Poker Accuracy: {}".format(accuracy4))
print(classification_report(y_test4, predictions_poker))









