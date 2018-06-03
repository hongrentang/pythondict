#!/usr/bin/env python3
import re
from datetime import datetime
from collections import Counter

def open_parser(filename):
    with open(filename) as logfile:
        pattern = ( r''
                    r'(\d+.\d+.\d+.\d+)\s-\s-\s'
                    r'\[(.+)\]\s'
                    r'"GET\s(.+)\s\w+/.+"\s'
                    r'(\d+)\s'
                    r'(\d+)\s'
                    r'"(.+)"\s'
                    r'"(.+)"'
                    )
        parsers = re.findall(pattern,logfile.read())


    return parsers


def date_format(string): 
    log_date = datetime.strptime(string,'%d/%b/%Y:%H:%M:%S %z').strftime('%Y-%m-%d')
    return log_date



def max_ip_dict(logs,parameter,file1,file2):
        
    loglist = []
    for row  in logs:
        log_date = date_format(row[file1])
        if  log_date  == parameter:
            loglist.append(row[file2])
    c = Counter(loglist)
    max_num = c.most_common(1)
    max_dict = {}
    for k,v in max_num:
        max_dict[k] = v

    return max_dict


def max_url_dict(logs,parameter,file1,file2):
        
    loglist = []
    for row  in logs:
        if  row[file1]  == parameter:
            loglist.append(row[file2])
    c = Counter(loglist)
    max_num = c.most_common(1)
    max_dict = {}
    for k,v in max_num:
        max_dict[k] = v

    return max_dict

def main():
    logs = open_parser('/home/shiyanlou/Code/nginx.log')
    ip_dict = max_ip_dict(logs,'2017-01-11',1,0)
    url_dict = max_url_dict(logs,'404',3,2)
    return ip_dict,url_dict


if __name__ == '__main__':
    ip_dict, url_dict = main()
    print(ip_dict,url_dict)


