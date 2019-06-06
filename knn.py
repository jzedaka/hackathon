###############################
# knn.py
###############################

import numpy as np

class Knn:

    def __init__(self, k):
        self.__k = k

    def fit(self, X, y):
        self.__X = X
        self.__y = y

    def predict(self, x):
        distances = np.linalg.norm(self.__X - x, axis=1)
        k_n_n_indexes = np.argsort(distances, axis=0)[:self.__k]

        labels_sum = np.zeros(10)
        for i in k_n_n_indexes:
            labels_sum[self.__y[i]] += 1

        max_label = np.argsort(labels_sum)[-1]
        return max_label
    
    def predict_set(self, X):
        predictions = np.zeros(len(X))
        for i, x in enumerate(X):
            predictions[i] = self.predict(x)

        return np.array(predictions)

    def accuracy(self, X, y):
        predictions = self.predict_set(X)
        return np.sum(predictions == y) / len(y)