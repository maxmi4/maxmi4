#!/usr/bin/env python3


import sys

try: 
    if len(sys.argv) == 2:
        a = int(sys.argv[1]) # a=salary

        b = a - 3500  # b is should take tax

        if b <= 1500:
            c = b*0.03
            c = format(c,".2f")
            print(c)

        elif b>1500 and b<=4500:
            c = b*0.1-105
            c = format(c,".2f") 
            print(c)

        elif b>4500 and b<=9000:
            c = b*0.2-555
            c = format(c,".2f")
            print(c)

        elif b>9000 and b<=35000:
            c = b*0.25-1005
            c = format(c,".2f")
            print(c)

        elif b>35000 and b<=55000:
            c = b*0.3-2755
            c = format(c,".2f")
            print(c)

        elif b>55000 and b<=80000:
            c = b*0.35-5505
            c = format(c,".2f")
            print(c)

        elif b > 80000:
            c = b*0.45-13505
            c = format(c,".2f")
            print(c)

    else:
        raise ValueError()   
except ValueError:
    print("Parameter Error")
