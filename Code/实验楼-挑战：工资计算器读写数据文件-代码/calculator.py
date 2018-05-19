#!/usr/bin/env python3
import sys
import os.path
import csv
class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]
    def _handle(self,parameter):
        if parameter in self.args:
             try:
                 filename = self.args[self.args.index(parameter)+1]
                 if filename:
                     return filename
             except:
                  print("Parameter Error")
                  sys.exit(-1)
    def arg(self):
         filenamelist=[]
         for i in ['-c','-d','-o']:
             filename=self._handle(i)
             if filename:
                 filenamelist.append(filename)
         if len(filenamelist) == 3:
             return filenamelist
         else:
             print("Parameter Error")
             sys.exit(-1)       

class Config(object):
    def __init__(self,configfile):
         self.configfile = configfile
    def read_config(self):
         with open(self.configfile) as file:
             config={}
             for line in file:
                 try:

                     key,value = line.split('=')
                     config[key.strip()] = float(value.strip())
                 except:
                     print('configfile Formatting Error')
             return config

class UserData(object):
    def __init__(self,userfile):
        self.userfile = userfile
    def read_users_data(self):
        with open(self.userfile) as file:
            userdata=[]
            userdatacsv = csv.reader(file)
            for line in userdatacsv:
                try:
                    work_nmb,wages=line
                    userdata.append((work_nmb,wages))
                except:
                    print('userfile work_nmb:{} Formatting Error'.format(work_nmb))
        return userdata
class IncomTaxCalculator(object):
    tax_tr=3500
    def __init__(self,configdict,userdatalist):
        self.configdict = configdict
        self.userdatalist = userdatalist
        
    
    def ssccalculator(self,wages):
        jishuh = self.configdict['JiShuH']
        jishul = self.configdict['JiShuL']
        if wages > jishuh:
            wages = jishuh
        if wages < jishul:
            wages = jishul
        ssc_cost = wages * (self.configdict['YangLao']
                            + self.configdict['YiLiao']
                            + self.configdict['ShiYe']
                            + self.configdict['GongShang']
                            + self.configdict['ShengYu']
                            + self.configdict['GongJiJin']
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
 
    def calc_for_all_userdata(self):
        user_wages_info_list=[]
        for userinfo in self.userdatalist:
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
                            float('%.2f' %income)
                            )
            user_wages_info_list.append(user_wages_info)
        return user_wages_info_list
    def export(self,default='out.csv'):
            result = self.calc_for_all_userdata()
            with open(default,'w') as f:
                writer = csv.writer(f)
                writer.writerows(result)



if __name__ == '__main__':
    args = Args()
    configfile,userfile,outfile = args.arg()
    if os.path.exists(configfile):
        config = Config(configfile)
        configdict = config.read_config()
    else:
        print("{}Not found file".format(configfile()))
        sys.exit(-1)
    if os.path.exists(userfile):
        userdata = UserData(userfile)
        userdatalist = userdata.read_users_data()
    else:
        print("{} Not found file".format(userfile))
        sys.exit(-1)
    calculator = IncomTaxCalculator(configdict,userdatalist)
    calculator.export(outfile)
