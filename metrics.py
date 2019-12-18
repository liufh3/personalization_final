import numpy as np

def mae(true, pred):
    '''
    true: as a vector
    pred: as a vector
    calculating mean absolute error
    '''
    assert len(true) == len(pred)
    return np.mean(np.abs(true - pred))


def mse(true, pred):
    '''
    true as a vector
    pred as a vector
    calculating mean square error
    '''
    assert len(true) == len(pred)
    return np.mean(np.abs(true - pred) * np.abs(true - pred))


def get_rank(sum_dict, arraylike):
    score = arraylike['stars']
    user = arraylike['user_id']
    return sum_dict[user][int(score + 0.5) - 1]


def get_rank_pred(sum_dict, arraylike):
    score = arraylike['prediction']
    user = arraylike['user_id']
    return sum_dict[user][int(score + 0.5) - 1]


def rank_accuracy(sum_dict, prediction):
    '''
    input prediction dataframe and make user_id as index
    '''
    rank_true = prediction.apply(lambda x: get_rank(sum_dict, x), axis=1)
    rank_pred = prediction.apply(lambda x: get_rank_pred(sum_dict, x), axis=1)
    return np.corrcoef(rank_true, rank_pred)[0][1]

def get_metrics(pred_df,sum_dict):
    return (mae(pred_df['stars'],pred_df['prediction']),
            mse(pred_df['stars'],pred_df['prediction']),
            rank_accuracy(sum_dict,pred_df))