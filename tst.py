a=open('new.txt')
cnt = 0
fl = list()
for i in a:
    val1=i.strip()
    val1=val1.split()
    print('1',val1)
    if cnt == 0:
        cnt =1
        val2=val1
        continue
    print('2',val2)
    for x in val2:
        print('x value :',x)
    #    for x in val1:
    #        print('cntn',x)
    #        break
        val1=val2+val1
        print('inside: ',x)
        print('val1',val1)
#    c=d+c
    #print('add',c)
    #fl.append(c)
    val2=val1
    print('end',val2)
#fl.append(c)
#xx=fl.split()
print('final',val1)
