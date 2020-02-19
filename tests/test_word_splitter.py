from . import analysesprint as ansp
import pandas as pd
import numpy as np
import pytest
import pandas.testing as pdt

def test_split_tweets_dataframe():
    
    assert ansp.word_splitter(ansp.twitter_df.copy()).loc[0, "Split Tweets"] 
            == ['@bongadlulane', 'please', 'send', 'an', 'email', 'to',
                'mediadesk@eskom.co.za']

    assert ansp.word_splitter(ansp.twitter_df.copy()).loc[1, "Split Tweets"] 
            == ['@saucy_mamiie', 'pls', 'log', 'a', 'call', 'on', '0860037566']

    assert ansp.word_splitter(ansp.twitter_df.copy()).loc[2, "Split Tweets"] 
            == ['@bongadlulane', 'query', 'escalated', 'to', 'media', 'desk.']

    assert ansp.word_splitter(ansp.twitter_df.copy()).loc[3, "Split Tweets"]
            == ['before', 'leaving', 'the', 'office', 'this', 'afternoon,', 'heading', 
                'off', 'into', 'the', 'weekend,', 'remember', 'to', 'switch', 'off', 
                'lights', '&amp;', 'electrical…', 'https://t.co/jug75zddaf']