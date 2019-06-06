###############################
# 
###############################

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, KFold
from sklearn.ensemble import AdaBoostClassifier
from feture_extractor import Feture_Extractor
from sklearn.tree import DecisionTreeClassifier
from knn import Knn
from common_words import count_key_words

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

def main():
    iter = 2
    df = load_data()
    accuracy = 0
#    most_used_words = set()
#    for i in range(len(names)):
#        most_used_words.update(count_key_words(names[str(i)]['tweet'], 30))

    for i in range(iter):
        train_x, train_y, test_x, test_y = split_data(df)
        kf = KFold(n_splits=8)
        #folds = kf.split(train_x)
        #print(folds)
        most_used_words = set(count_key_words(train_x, 350))
        extractor = Feture_Extractor(most_used_words)
        train_x = extractor.analyze_data(train_x)
        test_x = extractor.analyze_data(test_x)
        knn = Knn(k=30)
        knn.fit(train_x, train_y)
        accuracy += knn.accuracy(test_x, test_y)

        #adaboost = AdaBoostClassifier(
        #    base_estimator=DecisionTreeClassifier(max_depth=2),
        #    n_estimators=200)
        #adaboost.fit(train_x, train_y)
        #accuracy += adaboost.score(test_x, test_y)


    print(",", accuracy / iter)

if __name__ == "__main__":
    main()