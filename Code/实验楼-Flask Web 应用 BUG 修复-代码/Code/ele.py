# -*- coding: UTF-8 -*-

import re
import urllib
import requests

def ele_red_packet(number):
    s = requests.session()
    url = "http://www.quanmama.com/quan/2362429.html"
    user_agent = 'User-Agent: Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 MicroMessenger/6.5.13.1081 NetType/WIFI Language/zh_CN'
    headers = {'User-Agent': user_agent}
    s1 = r"group_sn=\w{32}"
    s2 = re.findall(s1, s.get(url, headers=headers).text)
    headers = {'User-Agent': user_agent,
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'text/plain;charset=UTF-8',
            "Host": "restapi.ele.me",
            "Origin": "https://h5.ele.me",
            "Pragma": "no-cache",
            "Referer": "https://h5.ele.me/baida/"
            }

    phone = number

    s3_list = []
    for sn in s2:
        value = {
            "group_sn": sn[9:],
            "phone": phone,
            "weixin_uid": '468015ki5tulqs9mbjmjvr6w83o45kh9'
        }
        s3 = s.post("https://restapi.ele.me/marketing/hongbao/h5/grab",
                    json=value, headers=headers)

        if "hongbao_list" in s3.text:
            s3_list.append(s3.status_code)


    if 200 in s3_list:
        return f"领取成功，{len(s3_list)} 个红包已注入 {phone} 的饿了么账户!"
    else:
        return "红包领取失败！"