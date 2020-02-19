# team_two_analyse
This package creates seven functions for Eskom data. The seven functions a Metric Dictionary, Five Number Summary, Date Parser, Municipality and Hashtag Detector, Number of tweets per day, Word Splitter and Stop Words.  

#Prerequisites
Import pandas
Import numpy
import pandas.testing

## building this package locally
'python setup.py sdist'

## installing this package from GitHub
'pip install git+https://github.com/wn-zarathustra/team2-analyse-sprint

##Updating this package
pip install --upgrade git+https://github.com/wn-zarathustra/team2-analyse-sprint

##Tests
For successful tests no response will be printed, failed tests will generate an error message.

test_dictionary_of_metrics: checks that the values returned for mean, median, variance, standard deviation, minimum and maximum values are correct.

test_five_num_summary: checks that the values returned for median, minimun and maximum values, first quartile and third quartile are correct.

test_date_parser: checks that the date has been split from this format 'yyyy-mm-dd hh:mm:ss 'and returns the date in this format 'yyyy-mm-dd'.

test_municipality_hashtags: checks that the correct municipality and hashtags have been extracted from the first 20 entries in a datframe.

test_number_of_tweets_per_day: checks if the number of tweets returned are equal to the the number of tweets counted per day.

test_word_splitter: checks that the list of words returned is the same as the list of words split from a sentence in each row in a dataframe.

test_stop_words_remover: checks that the correct words from a tweet are removed according to stop_words_dict.

##Authors
Ahmed Jaffer, Luvuyo Nkosana, Wright Nyoka, Zintle Faltein-Maqubela

##License 
This package is licensed under the MIT License.