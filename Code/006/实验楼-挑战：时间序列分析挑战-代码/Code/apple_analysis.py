# _*_ coding:utf-8 _*_

import pandas as pd

def quarter_volume():
    data = pd.read_csv('apple.csv',index_col=0)
    data.index = pd.to_datetime(data.index)
    second_volume = data.resample('Q').sum().sort_values('Volume',ascending=False).iloc[1]['Volume']
    return second_volume

if __name__ == '__main__':
    result = quarter_volume()
    print(result)
