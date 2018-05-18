#!/usr/bin/env python3
#coding=utf-8

#导入sys模块
import sys
#判断执行该脚本是否为2个惨数

if len(sys.argv) == 2:
    # 定义一个变量salary接受sys.argv[1]并转为int类型
    try:
        salary = int(sys.argv[1])
    except:
        print('Parameter Error')
else:
    print('缺少参数或参数过多')
#定义exceed 超起征税额数
if salary > 3500:
    exceed = salary - 3500
    if exceed > 80000:
	    tax = exceed * 0.45 - 13505
    elif exceed > 55000:
	    tax = exceed * 0.35 - 5505
    elif exceed > 35000:
	    tax = exceed * 0.30 - 2755
    elif exceed > 9000:
	    tax = exceed * 0.25 - 1005
    elif exceed > 4500:
	    tax = exceed * 0.20 - 555
    elif exceed > 1500:
	    tax = exceed * 0.10 - 105
    else:
	    tax = exceed * 0.03
    print("{:.2f}".format(tax))
else:
    print('no need to pay taxes')
