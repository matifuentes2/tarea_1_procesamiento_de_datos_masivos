import numpy as np
import re
from nltk.corpus import stopwords
from math import floor
import pickle 
from collections import Counter
import pickle

#https://stackoverflow.com/questions/33404752/removing-emojis-from-a-string-in-python
def remove_emojis(text):
    """
    Devuelve texto (idealmente) sin emojis
    """
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', text)

stopwords = set(stopwords.words('spanish'))
stopwords_dict = Counter(stopwords)


#https://stackoverflow.com/questions/25346058/removing-list-of-words-from-a-string
def filter_sentence(text):
    querywords = text.split()
    resultwords  = [word for word in querywords if word.lower() not in stopwords_dict]
    result = ' '.join(resultwords)
    return result

def get_shingles(text):
    k = 5
    result = set()
    for i in range(len(text) - k-1):
        shingle =  text[i:i+k] # By character
        result.add(shingle)
    return result

# # Quitar caracteres raros
# def remove_weird(text):
#     return ''.join([c for c in text if ord(c) < 128])

# Aplicar todas las funciones anteriores
def string_clean_pipeline(text):
    text = remove_emojis(text)
    text = filter_sentence(text)
    return text

def pre_process(chunk, indice, prev_max_index):
    resumen = chunk
    resumen['text'].str.lower().str.contains("rt @")
    resumen = resumen[~resumen['text'].str.lower().str.contains("rt @|http", regex=True)] # quitar retweets
    #resumen = resumen.reset_index().iloc[:, 1:]
    resumen["clean_text"] = np.vectorize(string_clean_pipeline)(resumen["text"])
    
    tweet_len = resumen.clean_text.apply(len)
    resumen = resumen[tweet_len>40] # Quitar tweets demasiado cortos
    resumen = resumen.reset_index().iloc[:, 1:]
    resumen.index = resumen.index.map(lambda x: x + prev_max_index)
    max_index = resumen.index.max()

    resumen["shingles"] = np.vectorize(get_shingles)(resumen.clean_text)
    resumen = resumen.drop("clean_text", axis = 1)
    shingles_dict = resumen.shingles.to_dict()
    resumen = resumen.drop('shingles', axis = 1)
    with open(f'processed_tweets/resumen{indice}.obj', 'wb') as filehandler:
        pickle.dump(resumen, filehandler)
    return (shingles_dict, max_index)

# def fast_hash_to_float(message):
#     message_bytes = message.encode('utf-8')
#     hash_object = xxhash.xxh64(message_bytes)
#     return hash_object.intdigest() / 2**64

