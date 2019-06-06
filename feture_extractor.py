import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

KEY_WORDS = ['!','#','$','@',',','.', '\n', '?','jimmy','kimmel', 'trump','vp','biden',
         'kim', 'maga', 'kanye','ellen', 'kard', 'king',' james', 'kkw', 'found', 'conan']
NUM_OF_FETURES = len(KEY_WORDS) + 3

class Feture_Extractor():

    def analyze_tweet(self, tweet):
        fetures = np.zeros(NUM_OF_FETURES)

        for i, word in enumerate(KEY_WORDS):
            fetures[i] = tweet.lower().count(word)

        fetures[i+1] = sum(1 for c in tweet if c.isupper())
        fetures[i+2] = len(tweet)
        fetures[i+3] = sum(c.isdigit() for c in tweet)

        return fetures

    def analyze_data(self, data):
        fetured_data = []
        for tweet in data:
            fetured_data.append(self.analyze_tweet(tweet))
        
        return np.array(fetured_data)
