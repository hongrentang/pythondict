#!/usr/bin/env python3

import json

import pandas as pd


def analysis(file,user_id):
    counts = 0
    minutes = 0
    with open(file) as f:
        data = f.read()

    pd_data = pd.DataFrame(json.loads(data))
    counts = pd_data[pd_data['user_id'] == user_id]['user_id'].count()
    minutes = pd_data[pd_data['user_id'] == user_id]['minutes'].sum()
    return counts,minutes



if __name__ == '__main__':
    result = analysis('user_study.json',1)
    print (result)


