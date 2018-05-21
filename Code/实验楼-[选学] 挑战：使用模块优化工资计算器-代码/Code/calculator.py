#!/usr/bin/env python3
import sys
import os.path
import getopt
import configparser
import csv
import datetime
from multiprocessing import Process,Queue
def args():
    cityname = ''
    configfile = ''
    userdata = ''
    resultdata= ''
    if len(sys.argv) <2:
        print("Usage:calculator.py -h",end='')
    try:
        options,args= getopt.getopt(sys.argv[1:],"hC:c:d:o:")
        for k,v in options:
	    #print(k)
            if k == '-h':
                 print("Usage:calculator.py -C cityname -c configfile -d userdata -o resultdat",end='')
            if k == '-C':
                 cityname = v
            if k == '-c':
                 configfile = v
            if k == '-d':
                 userdata = v
            if k == '-o':
                 resultdata = v
  
    except getopt.GetoptError as e:
        print(e)
        print("Usage:calculator.py -h",end='')

    
    return cityname,configfile,userdata,resultdata       

def config(configfile,cityname='DEFALUT'):
    config = configparser.ConfigParser()
    try:
        config.read(configfile)
        configlist=config.items(cityname.upper())
    except configparser.NoSectionError:
        print('no found configer')
    configdict={}
    for i in configlist:
        k,v = i
        configdict[k]=v
    return configdict


class UserData(object):
    def __init__(self,userfile):
        self.userfile = userfile
    def read_users_data(self,queue1):
        with open(self.userfile) as file:
            userdata=[]
            userdatacsv = csv.reader(file)
            for line in userdatacsv:
                try:
                    work_nmb,wages=line
                    userdata.append((work_nmb,wages))
                except:
                    print('userfile work_nmb:{} Formatting Error'.format(work_nmb))
        queue1.put(userdata)
  
        
class IncomTaxCalculator(object):
    tax_tr=3500

    def __init__(self,configdict):
        self.configdict = configdict
         
    def ssccalculator(self,wages):
        jishuh = float(self.configdict['jishuh'])
        jishul = float(self.configdict['jishul'])
        if wages > jishuh:
            wages = jishuh
        if wages < jishul:
            wages = jishul
        ssc_cost = wages * (float(self.configdict['yanglao'])
                            + float(self.configdict['yiliao'])
                            + float(self.configdict['shiye'])
                            + float(self.configdict['gongshang'])
                            + float(self.configdict['shengyu'])
                            + float(self.configdict['gongjijin'])
                            )
        return ssc_cost
    def taxcalculator(self,tax_inc):
        fex_iac =((80000,0.45,13505),
                  (55000,0.35,5505),
                  (35000,0.30,2755),
                  (9000,0.25,1005),
                  (4500,0.20,555),
                  (1500,0.10,105),
                  (0,0.03,0)
                 )
        for line in fex_iac:
            x,y,z = line
            if tax_inc > x:
                tax = tax_inc * y -z
                return tax
            else:
                continue
 
    def calc_for_all_userdata(self,queue1,queue2):
        userdatalist = queue1.get()
        user_wages_info_list=[]
        for userinfo in userdatalist:
            work_nmb,wages = userinfo
            wages = int(wages)
            ssc_cost = self.ssccalculator(wages)
            tax_inc = wages - ssc_cost - IncomTaxCalculator.tax_tr
            if tax_inc >0 :
                 tax = self.taxcalculator(tax_inc)
            else:
                 tax = 0
            income = wages - ssc_cost - tax
            user_wages_info=(work_nmb,wages,
                            float('%.2f' %ssc_cost),
                            float('%.2f' %tax),
                            float('%.2f' %income),
                            datetime.datetime.now().strftime('%Y-%m-%d %H:%M%S')
                            )
            user_wages_info_list.append(user_wages_info)
        queue2.put(user_wages_info_list)
      
        
        
def export(queue2,default='out.csv'):
    result = queue2.get()
    with open(default,'w') as f:
        writer = csv.writer(f)
        writer.writerows(result)

                
def main(configdict,userdata,resultdata):
    queue1 = Queue()
    queue2 = Queue()
    userdata = UserData(userdata)
    calculator = IncomTaxCalculator(configdict)
    Process(target = userdata.read_users_data,args=(queue1,)).start()
    Process(target = calculator.calc_for_all_userdata,args=(queue1,queue2)).start()
    Process(target =  export,args=(queue2,resultdata)).start()    

if __name__ == '__main__':
    cityname,configfile,userdata,resultdata=args()
    if configfile:
        if cityname:
            configdict = config(configfile,cityname)
        else:
            configdict = config(configfile)
    else:
        print('not no confgfile')
    if userdata:
        if os.path.exists(userdata):
            main(configdict,userdata,resultdata)
    else:
        print('not no userdatafile')
