import string

file = 'mbox-short.txt'

o_file = open(file)

dct = dict()
lst = list()
dct1 = dict()
for i in o_file:
    spl = i.strip()
    spl = spl.split()
    #print(spl)
    if len(spl) == 0:
        continue
    if spl[0] == 'From':
        lst = spl[5]
        lst = lst.split(':')
        dct[lst[0]] = dct.get(lst[0],0)+1

tmp = list()
for v,k in dct.items():
    newt = (v,k)
    tmp.append(newt)
    #print (tmp)

tmp.sort(reverse=False)
for f in tmp :
    print(f[0],f[1])

#print (tmp)
