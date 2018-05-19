#!/usr/bin/env python3
#coding=utf-8
import sys
'''
:依法缴纳的社会保险
:return social_sum
'''
def social_sec(wages):
    ratelist = [0.08,0.02,0.005,0,0,0.06]
    social_sum =  wages * sum(ratelist)
    return social_sum
'''
:计算应缴纳的税额
:return tax
'''
def calculation(wages):
    social = social_sec(wages)
    tax_inc = wages - social - 3500
    if tax_inc > 0 :
        if tax_inc > 80000:
            tax = tax_inc * 0.45 - 13505
        elif tax_inc > 55000:
            tax = tax_inc * 0.35 - 5505
        elif tax_inc > 35000:
            tax = tax_inc * 0.30 - 2755
        elif tax_inc > 9000:
            tax = tax_inc * 0.25 - 1005
        elif tax_inc > 4500:
            tax = tax_inc * 0.20 - 555
        elif tax_inc > 1500:
            tax = tax_inc * 0.10 - 105
        else:
            tax = tax_inc * 0.03
        return tax,social
    else:
        #print("工作还不满足缴税条件，请继续努力工作哦！")   
        return 0,social

def man():
    #staffs = []
    for args in sys.argv[1:]:
        try:
            work_number,wages = args.split(':')
            wages = int(wages)
            tax,social = calculation(wages)
            income = wages - tax -social
            print('{}:{:.2f}'.format(work_number,income))
        except ValueError:
            print("Parameter Error")





if __name__=='__main__':
    if len(sys.argv) < 2:
        print("Paramenter Error") 
        sys.exit()
    else:
        man()
		 

