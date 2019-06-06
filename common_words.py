import collections
import pandas as pd
import matplotlib.pyplot as plt
#import nltk
#from nltk.corpus import stopwords
    # %matplotlib inline


def count_key_words(tweets, n):
    """counts the n most common words used in each tweet
    
    Arguments:
        tweets {[type]} -- [description]
        n {int} -- number of most counted words per tweet
    """
    stopwords_list = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you",
                      "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself",
                      "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
 #   stopwords_list = list(stopwords.words('english'))
    stopwords_list.append("['rt")
    stopwords_list.append("[rt")

    # Instantiate a dictionary, and for every word in the file,  
    # Add to the dictionary if it doesn't exist. If it does, increase the count.
    wordcount = {}
    for tweet in tweets:
        # update this
        # To eliminate duplicates, remember to split by punctuation, and use case demiliters.
        for word in tweet.lower().split():
            word = word.replace(".","")
            word = word.replace(",","")
            word = word.replace(":","")
            word = word.replace("\"","")
            # word = word.replace("!","")
            # word = word.replace("â€œ","")
            # word = word.replace("â€˜","")
            word = word.replace("*","")
            if word not in stopwords_list:
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1
        # Print most common word
    word_counter = collections.Counter(wordcount)
    kak = []
    for word, count in word_counter.most_common(n):
        kak.append(word)
    return kak

