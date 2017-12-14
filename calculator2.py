#!/usr/bin/env python3

import sys

#count sebao
def countsebao(salary):
    global sebao
    int(salary)
    sebao = salary*0.08+salary*0.02+salary*0.005+salary*0.06
    return sebao

#count ge ren suo de sui
def countynse(s):
    int(s) 
    int(sebao)
    global ynse
    ynsds = s-sebao-3500
    if ynsds <= 1500:
        ynse = ynsds*0.03
    elif 1500<ynsds and ynsds<=4500:
        ynse = ynsds*0.1-105
    elif 4500<ynsds and ynsds<=9000:
        ynse = ynsds*0.2-555
    elif 9000<ynsds and ynsds<=35000:
        ynse = ynsds*0.25-1005
    elif 35000<ynsds and ynsds<=55000:
        ynse = ynsds*0.3-2755
    elif 55000<ynsds and ynsds<=80000:
        ynse = ynsds*0.35-5505
    elif ynsds > 80000:
        ynse = ynsds*0.45-13505
    return ynse

try:
    for arg in sys.argv[1:]:
        b=arg.split(":")
        num = b[0]
        Mon = b[1]
        num = int(num)
        Mon = int(Mon)
        countsebao(Mon)
        countynse(Mon)
        if ynse <= 0:
            getsalary = Mon-sebao
        elif ynse > 0:
            getsalary = Mon-sebao-ynse
        getsalary = format(getsalary,".2f")
        print(num,end=':')
        print(getsalary)
except IndexError:
    print("Parameter Error")
except ValueError:
    print("Parameter Error")
