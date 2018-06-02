#!/usr/bin/env python3
import sys
from pymongo import MongoClient
'''
计算每个用户总的score,submit_time 返回一个字典
'''
def calculation(contests):

    data = {}
    for contest in contests:
        if data.get(contest['user_id']):
            data[contest['user_id']]['score'] = data.get(contest['user_id']).get('score')+contest['score']
            data[contest['user_id']]['submit_time'] = data.get(contest['user_id']).get('submit_time')+contest['submit_time']
        else:
            data[contest['user_id']]= {'score':contest['score'],'submit_time':contest['submit_time']}
    return data
'''
将字典转换成列表，方便排序
'''
def dict_to_list(datadict):
    datalist = []
    for data in datadict:
        datalist.append((data,[datadict[data]['score'],datadict[data]['submit_time']]))
    return datalist
'''
排序,采用冒泡排序,data[j][1][0] 与data[j+1][1][0]小的数据就是score向后沉,如果相同将比较data[j][1][1] 与data[j+1][1][1]大的数据 就是submit_time向后沉
'''
def list_sorted(data):
    for i in range(len(data) -1):
        for j in range(len(data) -i -1):
            if data[j][1][0] < data[j+1][1][0]:
                data[j],data[j+1] = data[j+1],data[j]
            elif data[j][1][0] == data[j+1][1][0]:
                if data[j][1][1] > data[j+1][1][1]:
                    data[j],data[j+1] = data[j+1],data[j]
    return data
    
'''
将列表转成字典，并加入排序名次
'''
def list_to_dict(data):
    dict_sort_data={}
    for i in data:
        x,y = i
        dict_sort_data[x]=[data.index(i)+1,y[0],y[1]]
        
    return dict_sort_data

def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    user_data=db.contests.find_one({'user_id':user_id})
    if  not user_data:
        print('该用户没有数据')
        sys.exit(0)
   
    contests = db.contests 
    contests = contests.find()
    if contests:
        datadict = calculation(contests)
        datalist = dict_to_list(datadict)
        sort_data = list_sorted(datalist)
        dict_sort_data = list_to_dict(sort_data)
        rank,score,submit_time = dict_sort_data.get(user_id)
        return rank,score,submit_time


if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
           user_id = int(sys.argv[1])
        except ValueError:
            print("Paramenter Error")
            sys.exit(0)
        userdata = get_rank(user_id)
        print(userdata)
    else:
        print("Paramenter Error")


