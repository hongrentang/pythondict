#!/usr/bin/env python3

import sys
import socket
import getopt
import re

def connect(host,port):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.settimeout(0.1)
        code = s.connect_ex((host,port))

    return code
'''
正则匹配host的ip合法
'''
def ip_re(host):
    patter = re.compile('((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))')
    result = re.fullmatch(patter,host)
    if result:
       return  result.group(0)
'''
判断端口合法性：0－65535
'''
def port_re(port):
    patter = re.compile('([0-9]|[1-9]\d{1,3}|[1-5]\d{4}|6[0-5]{2}[0-3][0-5])')
    result = re.fullmatch(patter,port)
    if result:
        return result.group(0)
'''
参数处理
'''
def args():
    host = None
    port = None
    try:
        opts,ags = getopt.getopt(sys.argv[1:],'hH:P:',["help","host=","port="])
    except getopt.GetoptError:
        print('usage: python3 %s --host xxx.xxx.xxx.xxx --port xxx|xxx-xxx' % __name__)
        sys.exit(0) 

    for k,v in opts:
        if k in ("-h","--help"):
            print('usage: python3 %s --host xxx.xxx.xxx.xxx --port xxx|xxx-xxx' % __name__)
            sys.exit(0)
        elif k in ("-H","--host"):
            host = v
        elif k in ("-P","--port"):
            port = v
        else: 
            print('usage: python3 %s --host xxx.xxx.xxx.xxx --port xxx|xxx-xxx' % __name__)
            sys.exit(0)

    if host and port:        
         return host,port
    else:    
        print('usage: python3 %s --host xxx.xxx.xxx.xxx --port xxx|xxx-xxx' % __name__)
        sys.exit(0)

'''
检查端口合法性
'''
def port_check(port):
    port = port_re(port)
    if port:
        try:
            port = int(port)
        except ValueEroor:
            print("Paramenter Error")
            sys.exit(2)

        return port
    else:
        print("Paramenter Error")
        sys.exit(2)

'''
打印结果
'''
def print_result(port,code):
    if code == 0 :
        print('{} open'.format(port))
    else:
        print('{} closed'.format(port))

def man():
    host,port = args()
    host = ip_re(host)
    if not host:
        print("Parameter Error")
        sys.exit(2)

    #带－的端口
    if '-' in port :
        sport,eport= port.split('-')
        sport = port_check(sport)
        eport = port_check(eport)
        for port in range(sport,eport+1):
            code=connect(host,port)
            print_result(port,code)
    else:
        port = port_check(port)
        code = connect(host,port)
        print_result(port,code)


if __name__ == '__main__':
    man()


