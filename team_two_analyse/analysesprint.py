import pandas as pd
import numpy as np
import pandas.testing as pdt

ebp_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv'
ebp_df = pd.read_csv(ebp_url)

for col, row in ebp_df.iloc[:,1:].iteritems():
    ebp_df[col] = ebp_df[col].str.replace(',','').astype(int)

twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
twitter_df = pd.read_csv(twitter_url)

# gauteng ebp data as a list
gauteng = ebp_df['Gauteng'].astype(float).to_list()

# dates for twitter tweets
dates = twitter_df['Date'].to_list()

# dictionary mapping official municipality twitter handles to the municipality name
mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
}

# dictionary of english stopwords
stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose', 
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', 
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', 
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under', 
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves', 
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', 
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', 
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty', 
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', 
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our', 
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', 
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
}

def dictionary_of_metrics(items):
    """
    Function will calculate the metrics for the data.

    Arguments:  
            (items): list containing numerical values.

    Returns:
            a dictionary of the metrics with mean,
            median, variance, standard deviation,
            minimum and maximum values.
    """

    metrics = {'mean': round(np.mean(items), 2),
               'median': round(np.median(items), 2),
               'var': round(np.var(items, ddof=1), 2),
               'std': round(np.std(items, ddof=1), 2),
               'min': min(items), 'max': max(items)
               }

    return metrics

def five_num_summary(items):
    """
    Function will return the five number summary for the data.

    Arguments:
            (items): list of integers.

    Returns :
            a dictionary of the five number summary with
            the maximum and minimum values, median, first quartile 
            and third quartile.
    """

    summary = {'max': max(items),
               'median': np.median(items),
               'min': min(items),
               'q1': np.quantile(items, 0.25),
               'q3': np.quantile(items, 0.75)
               }

    return summary
    
def date_parser(list_dates):
    """ 
    Function will split the date and time

    Arguments:
            (list_dates): list of date and time
            in the format 'yyyy-mm-dd hh:mm:ss'

    Returns:
            a new list in the format 'yyy-mm-dd'
    """
    #Splits input into a list
    #And returns a list of the first value in the split
    return [(item.split(" ")[0]) for item in list_dates]

def extract_municipality_hashtags(df):
    """ 
    Function will return information about the municipality and hashtag from twitter data.

    Arguments:
            (df): pandas dataframe.

    Returns :
            a new dataframe with columns for municipality and hashtags.

    Additional information
    -------------------
    the function relies on the dictionary mun_dict 
    """

    municipalityKeys = list(mun_dict.keys())
    municipalities = []
    hashtags = []
    
    #Iterates through each row in the DataFrame
    for index, row in df.iterrows():
        municipalities.append(np.nan)
        #Splits each tweet into a list of separate words
        tweet = row['Tweets'].split()
        tags = []
        #Iterates through each word in the tweet list
        for word in tweet:
            #Extracts all hashtags from list
            if word.startswith('#'):
                tags.append(word.lower())
            #Extracts municipality name if present 
            if municipalityKeys.count(word):
                municipalities[index] = mun_dict[word]

        hashtags.append(tags) if tags else hashtags.append(np.nan)

    df['municipality'] = municipalities
    df['hashtags'] = hashtags

    return df

def number_of_tweets_per_day(df):
    """ 
    Function will count number of tweets per day

    Arguments:  
            takes a Pandas DataFrame as input

    Returns:    
            a new DataFrame grouped by day 
            (new column 'Date') with the 
            number of tweets for that day
    """

    df["Date"] = df["Date"].apply(lambda x: x.split(" ")[0])
    # performs the groupby and count actions and saves to return
    last_df = df[['Tweets', 'Date']].groupby(['Date']).count()

    return last_df

def word_splitter(df):
    """ 
    Function will split a sentence in a dataframe column into a list of the seperate words.

    Arguments:
            (df): Pandas DataFrame with twitter data

    Returns:
            a new dataframe with an added column for the list of the seperate words.
    """

    tokens = []
    #Iterates through each row in the DataFrame
    for index, row in df.iterrows():
        #Splits each tweet into a list of separate words
        #Convert each word to lower case
        #Appends the resulting list to the tokens list
        tokens.append(list(map(str.lower, row['Tweets'].split())))

    df['Split Tweets'] = tokens

    return df

def stop_words_remover(df):
    """ 
    Function removes stop words from a tweet.

    Arguments:
            (twitter_df): Pandas DataFrame with tweets

    Returns:
            a new dataframe with an added column for the tweets without stop words.

    Additional information
    -------------------
    the function relies on the dictionary stop_words_dict    
    """

    nstokens = []

    for index, row in df.iterrows():
        tempTokens = []
        #Splits each tweet into a list of separate words
        #Convert each word to lower case
        #Appends the resulting list to the tokens list
        for word in list(map(str.lower, row['Tweets'].split())):
            #Removes any stop words in the list
            if word not in stop_words_dict['stopwords']:
                tempTokens.append(word)
        nstokens.append(tempTokens)

    df['Without Stop Words'] = nstokens

    return df