a = input ('Please enter : ')
#catching exceptions......
try:
    a=int(a)
except :
    a = -1

#example with break and continue using while loop
while a > 0 :
    print(a)
    if a ==2:
        print('Brk')
        break
    if a ==4:
        a=a-1
        print('Cntn')
        continue
    a = a-1
print ('Done')
print(a)

#for loops...
f=('first','second')
for l in f :
    print ('value : ',l)
print ('Done')
