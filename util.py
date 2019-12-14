import pandas as pd
import json
from tqdm import tqdm_notebook
import collections

def load_json(file_name, save = True):
    lines = open("yelp_dataset/"+str(file_name)+".json").readlines()
    keys = list(json.loads(lines[0]).keys())
    content_dict = collections.defaultdict(list)
    for line in tqdm_notebook(lines):
        blob = json.loads(line)
        for k in keys:
            content_dict[k].append(blob[k])
    df = pd.DataFrame(content_dict)
    if save:
        df.to_csv(file_name+'.csv',index = 0)
    return df


def get_sum_count(train_df):
    count_dict = {}
    count_dict = dict(train_df[['user_id','stars']].groupby('user_id').apply(lambda x:dict(collections.Counter(x['stars']))))
    sum_dict = collections.defaultdict(list)
    for user in tqdm_notebook(count_dict.keys()):
        for star in [1,2,3,4,5]:
            sum_dict[user].append(count_dict[user].get(star,0))
        for i in range(4):
            sum_dict[user][i + 1] += sum_dict[user][i]