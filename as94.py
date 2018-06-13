file = 'mbox-short.txt'

o_file = open(file)

dct = dict()

for i in o_file:
    spl=i.strip()
    spl = spl.split()
    ln = len(spl)
    #print(ln)
    if ln == 0:
        continue
    #print(spl[0])
    if spl[0] == 'From' :
        #print(spl[1])
        dct[spl[1]] = dct.get(spl[1],0)+1
    else:
        continue

g_name = None
g_val = None

for k,v in dct.items():
    #print(k,' out ',v)
    if g_name is None or v > g_val:
        #print('in : ',k,' in ',v)
        g_name = k
        g_val = v

#print(dct)
print(g_name,': ',g_val)
