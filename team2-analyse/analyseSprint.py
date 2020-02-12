def dictionary_of_metrics(items):

  ### Code Here

  pass

def five_num_summ(items):

  ### Code Here

  pass

def date_parser(list_dates):

  ### Code Here

  pass

def extract_municipality_hashtags(df):
  municipalityKeys = list(mun_dict.keys())
  municipalities = []
  hashtags = []
  for index, row in df.iterrows():
      municipalities.append(np.nan)
      tweet = row['Tweets'].split()
      tags = []
      for word in tweet:
          if word.startswith('#'):
              tags.append(word.lower())
          if municipalityKeys.count(word): municipalities[index] = mun_dict[word] 
      hashtags.append(tags) if tags else hashtags.append(np.nan)
  df['municipality'] = municipalities
  df['hashtags'] = hashtags
  return df

def number_of_tweets_per_day(df):

  ### Code Here

  pass

def word_splitter(df):
  tokens = []
  for index, row in df.iterrows():
      tokens.append(list(map(str.lower, row['Tweets'].split())))
  df['Split Tweets'] = tokens
  return df

def stop_words_remover(df):
    nstokens = []
    for index, row in df.iterrows():
        tempTokens = []
        for word in list(map(str.lower, row['Tweets'].split())):
            if word not in stop_words_dict['stopwords']: tempTokens.append(word)
        nstokens.append(tempTokens)
    df['Without Stop Words'] = nstokens
    return df