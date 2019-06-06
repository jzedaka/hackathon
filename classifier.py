###############################
# classifier.py
###############################

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, KFold
from sklearn.ensemble import AdaBoostClassifier
from feture_extractor import Feture_Extractor
from sklearn.tree import DecisionTreeClassifier
from common_words import count_key_words
import matplotlib.pyplot as plt

K = [10, 20,30, 50,70]
names = {'0':'donaldTrump', '1':'joeBiden','2':'ConanOBrien','3':'ellenShow','4':'KimKardashian', '5':'labronJames',
                                                '6':'ladygaga', '7':'cristiano', '8':'jimmykimmel','9': 'Schwarzenegger' }
def split_data(df):
    train, test = train_test_split(df, train_size=0.75 , shuffle=True)
    train_y = np.array(train['user'])
    train_x = np.array(train['tweet'])
    test_y = np.array(test['user'])
    test_x = np.array(test['tweet'])

    return train_x, train_y, test_x, test_y

def load_data():
    df = pd.DataFrame()
    for i in range(len(names)):
        names[str(i)] = pd.read_csv("tweets_data/" + names[str(i)] + "_tweets.csv")
        df = df.append(names[str(i)])

    return df

def classify(input):
    df = load_data()

    train_x, train_y, test_x, test_y = split_data(df)
    most_used_words = set(count_key_words(train_x, 350))
    extractor = Feture_Extractor(most_used_words)

    train_x = extractor.analyze_data(train_x)
    #test_x = extractor.analyze_data(test_x)

    #knn = Knn(k)
    #knn.fit(train_x, train_y)
    #acc[j] += knn.score(test_x, test_y)

    adaboost = AdaBoostClassifier(
        base_estimator=DecisionTreeClassifier(max_depth=2),
        n_estimators=200)
    adaboost.fit(train_x, train_y)

    input = extractor.analyze_data(np.array(input))
    return adaboost.predict(input)

 #   except Exception as e:
  #      print(e)
    #   return [1] * len(input)
