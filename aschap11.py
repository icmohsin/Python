import re
file = 'regex_sum_99041.txt'
#file = 'new.txt'
o_file = open(file)
sm=0
for i in o_file:
    line = i.strip()
    #print(line)
    fnd = re.findall('[0-9]+',line)
    #print(fnd)
    if len(fnd) >0:
        for lp in fnd:
            sm = sm+int(lp)
            #print()
print(sm)
