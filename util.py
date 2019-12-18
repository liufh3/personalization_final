import pandas as pd
import json
import os
from tqdm import tqdm_notebook
import collections

def load_json(file_name, save = True):
    files = os.listdir('./yelp_dataset')
    if file_name + '.csv' not in files:
        lines = open("yelp_dataset/"+str(file_name)+".json").readlines()
        keys = list(json.loads(lines[0]).keys())
        content_dict = collections.defaultdict(list)
        for line in tqdm_notebook(lines):
            blob = json.loads(line)
            for k in keys:
                content_dict[k].append(blob[k])
        df = pd.DataFrame(content_dict)
        if save:
            df.to_csv("yelp_dataset/" + file_name+'.csv',index = 0)
    return


def get_sum_count(train_df):
    count_dict = dict(train_df[['user_id','stars']].groupby('user_id').apply(lambda x:dict(collections.Counter(x['stars']))))
    sum_dict = collections.defaultdict(list)
    for user in tqdm_notebook(count_dict.keys()):
        for star in [1,2,3,4,5]:
            sum_dict[user].append(count_dict[user].get(star,0))
        for i in range(4):
            sum_dict[user][i + 1] += sum_dict[user][i]
    return sum_dict


def clean_cate(x):
    if type(x) == str:
        res = []
        terms = x.split(',')
        for t in terms:
            res.append(t.strip().replace(' ', '_'))
        # print(res)
        return ' '.join(res)
    else:
        return ''
