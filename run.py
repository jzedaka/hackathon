###############################
# 
###############################

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from feture_extractor import Feture_Extractor
from knn import Knn

names = {'0':'donaldTrump', '1':'joeBiden','2':'ConanOBrien','3':'ellenShow','4':'KimKardashian', '5':'labronJames',
                                                '6':'ladygaga', '7':'cristiano', '8':'jimmykimmel','9': 'Schwarzenegger' }
def separate_data(df):
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
    iter = 1
    df = load_data()
    accuracy = 0

    for i in range(iter):
        print(i)
        train_x, train_y, test_x, test_y = separate_data(df)
        extractor = Feture_Extractor()
        train_x = extractor.analyze_data(train_x)
        test_x = extractor.analyze_data(test_x)
        knn = Knn(k=30)
        knn.fit(train_x, train_y)
        accuracy += knn.accuracy(test_x, test_y)

    print(accuracy / iter)

if __name__ == "__main__":
    main()