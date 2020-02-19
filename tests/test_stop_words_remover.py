from . import analysesprint as ansp
import pandas as pd
import numpy as np
import pytest
import pandas.testing as pdt

def test_stop_words_dataframe():
    assert ansp.stop_words_remover(ansp.twitter_df.copy()).loc[0, "Without Stop Words"] 
            == ['@bongadlulane', 'send', 'email', 'mediadesk@eskom.co.za']
        
    assert ansp.stop_words_remover(ansp.twitter_df.copy()).loc[1, "Without Stop Words"]
            == ['@saucy_mamiie', 'pls', 'log', '0860037566']
    
    assert ansp.stop_words_remover(ansp.twitter_df.copy()).loc[2, "Without Stop Words"]
            == ['@bongadlulane', 'query', 'escalated', 'media', 'desk.']
    
    assert ansp.stop_words_remover(ansp.twitter_df.copy()).loc[3, "Without Stop Words"]
            == ['leaving', 'office', 'afternoon,', 'heading', 'weekend,',
                 'remember', 'switch', 'lights', '&amp;', 'electrical…',
                'https://t.co/jug75zddaf']