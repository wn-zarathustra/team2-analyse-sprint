from . import analysesprint as ansp
import pandas as pd
import numpy as np
import pandas.testing as pdt

def test_metrics_for_gauteng():
    assert ansp.dictionary_of_metrics(ansp.gauteng) == {'mean': 26244.42,
                                              'median': 24403.5,
                                              'var': 108160153.17,
                                              'std': 10400.01,
                                              'min': 8842.0,
                                              'max': 39660.0}


def test_metrics_for_limpopo():
    assert ansp.dictionary_of_metrics(ansp.limpopo) == {'mean': 44105.33,
                                              'median': 44035.0,
                                              'var': 191294774.61,
                                              'std': 13830.94,
                                              'min': 18592.0,
                                              'max': 68121.0}


def test_metrics_for_western_cape():
    assert ansp.dictionary_of_metrics(ansp.western_cape) == {'mean': 22422.25,
                                              'median': 19349.5,
                                              'var': 169996562.02,
                                              'std': 13038.27,
                                              'min': 4639.0,
                                              'max': 48429.0}