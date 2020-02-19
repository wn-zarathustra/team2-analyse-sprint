from . import analysesprint as ansp
import pandas as pd
import numpy as np
import pytest
import pandas.testing as pdt

def test_tweets_per_day_dataframe():
    assert ansp.number_of_tweets_per_day(twitter_df.copy())['Tweets'].iloc[0] == 18
    assert ansp.number_of_tweets_per_day(twitter_df.copy())['Tweets'].iloc[1] == 11
    assert ansp.number_of_tweets_per_day(twitter_df.copy())['Tweets'].iloc[2] == 25
    assert ansp.number_of_tweets_per_day(twitter_df.copy())['Tweets'].iloc[3] == 19
    assert ansp.number_of_tweets_per_day(twitter_df.copy())['Tweets'].iloc[4] == 14
    
    try: 
        assert ansp.number_of_tweets_per_day(twitter_df.copy())['Tweets'].iloc[0] == 12
    except:        
        raise AssertionError('Failed Successfully')
    try: 
        assert ansp.number_of_tweets_per_day(twitter_df.copy())['Tweets'].iloc[2] == 12
    except:        
        raise AssertionError('Failed Successfully')
    try: 
        assert ansp.number_of_tweets_per_day(twitter_df.copy())['Tweets'].iloc[4] == 15
    except:        
        raise AssertionError('Failed Successfully'