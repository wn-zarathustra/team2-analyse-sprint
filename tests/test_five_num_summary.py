from . import analysesprint as ansp
import pandas as pd
import numpy as np
import pandas.testing as pdt

def test_five_number_summary_for_gauteng():
    assert ansp.dictionary_of_metrics(ansp.gauteng) == {'max': 39660.0,
                                              'median': 24403.5,
                                              'min': 8842.0,
                                              'q1': 18653.0,
                                              'q3': 36372.0}


def test_five_number_summary_for_limpopo():
    assert ansp.dictionary_of_metrics(ansp.limpopo) == {'max': 68121.0,
                                              'median': 44035.0,
                                              'min': 18592.0,
                                              'q1': 35670.5,
                                              'q3': 52556.5}


def test_five_number_summary_for_western_cape():
    assert ansp.dictionary_of_metrics(ansp.western_cape) == {'max': 48429.0,
                                                   'median': 19349.5,
                                                   'min': 4639.0,
                                                   'q1': 12007.75,
                                                   'q3': 29905.75}