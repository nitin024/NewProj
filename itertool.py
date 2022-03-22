import itertools
   
count = 0
   
# for in loop
for i in itertools.cycle('AB'):
    if count > 7:
        break
    else:
        print(i, end = " ")
        count += 1
        
Input:      
4
1
10
5
2
8
48
14
63
59
47
49
22
19
60
1
40