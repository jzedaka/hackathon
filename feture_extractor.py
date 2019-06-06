import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

KEY_WORDS = ['!','#','$','@',',','.', '\n', '?']
NUM_OF_FETURES = len(KEY_WORDS) + 3

class Feture_Extractor():

    def __init__(self, most_used_words):
        self._most_used_words = most_used_words

    def analyze_tweet(self, tweet):
        fetures = []

        for word in KEY_WORDS:
            fetures.append(tweet.lower().count(word))



        for word in self._most_used_words:
             fetures.append(tweet.lower().count(word.lower()))

        fetures.append(sum(1 for c in tweet if c.isupper()))
        fetures.append(len(tweet))
        fetures.append(sum(c.isdigit() for c in tweet))

        return fetures

    def analyze_data(self, data):
        fetured_data = []
        for tweet in data:
            fetured_data.append(self.analyze_tweet(tweet))
        
        return np.array(fetured_data)
