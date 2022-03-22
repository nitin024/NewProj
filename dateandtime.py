
#!/bin/python3
import math
import os
import random
import re
import sys


#
# Complete the 'dateandtime' function below.
#
# The function accepts INTEGER val as parameter.
# The return type must be LIST.
#
from datetime import datetime
def dateandtime(val,tup):
    ans=[]
    if val == 1:
        str1 = ''
        for item in tup:
            str1 = str1 + str(item) + '-'
        str2=str1[0:-1]
        
        a = datetime.strptime(str2,'%Y-%m-%d')
        b = a.date()
        ans.append(b)
        
        c = b.strftime("%d/%m/%Y")
        
        ans.append(c)
        return ans
    if val == 2:
        res = int(''.join(map(str, tup)))
        a = datetime.fromtimestamp(res)
        b = a.strftime('%Y-%m-%d %H:%M:%S')
        c = a.date()
        ans.append(c)
        return(ans)
    
    if val == 3:
        #print(val)
        #print(tup)
        str1 = ''
        for item in tup:
            str1 = str1 + str(item) + ':'
        str2=str1[0:-1]
        str2 = '01-01-2011 ' + str2
        #print(f'str2-->  {str2}')
        a = datetime.strptime(str2,"%d-%m-%Y %H:%M:%S")
        b = a.time()
        #print(b)
        ans.append(b)
        c = b.strftime("%I")
    
        ans.append(c)
        return ans
    
    if val == 4:
        str1 = ''
        for item in tup:
            str1 = str1 + str(item) + '-'
        str2=str1[0:-1]
        a = datetime.strptime(str2,'%Y-%m-%d')
        b = a.date()
        #c = b.weekday()
        c = a.strftime('%A')
        ans.append(c)
        
        d =  a.strftime('%B')
        ans.append(d)
        
        e = a.strftime('%j')
        ans.append(e)
        
        return ans
    
    if val == 5:
        #print(val)
        #print(tup)
        str1 = ''
        count = 1
        for item in tup:
            #print(count)
            if count < 3:
                str1 = str1 + str(item) + '-'
            elif count == 3:
                str1 = str1 + str(item) + ' '
            else:
                str1 = str1 + str(item) + ':'
            count+=1
        str2=str1[0:-1]
        a = datetime.strptime(str2,'%Y-%m-%d %H:%M:%S')
        
        ans.append(a)
        return ans
if __name__ == '__main__':
