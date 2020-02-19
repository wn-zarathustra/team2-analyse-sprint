from . import analysesprint as ansp
import pandas as pd
import numpy as np
import pytest
import pandas.testing as pdt

def test_hashtags_and_municipality_in_function_four_dataframe():

    muni_hashtags = ansp.extract_municipality_hashtags(ansp.twitter_df.copy().head(20))["hashtags"]
    hashtags = [np.nan, np.nan,np.nan,np.nan,
        ['#eskomfreestate', '#mediastatement'],np.nan,
        ['#fridaymotivation', '#eskomexpoisf'],['#eskommpumalanga'],
        np.nan,np.nan,['#fridaythoughts'],np.nan,np.nan,['#eskomnorthwest'],np.nan,['#poweralert'],
        ['#eskomfreestate', '#mediastatement'],np.nan,['#randburgoutage'],['#eskomgauteng', '#poweroutage']]

    hashtags_series = pd.Series(hashtags)
    
    hashtags_series = hashtags_series.rename('hashtags')
    
    pdt.assert_series_equal(muni_hashtags, hashtags_series)