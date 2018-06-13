a ='Hello how are you'
#a='123'
try:
    istr= int(a)
except:
    istr = -1
print(a)

type(a)

a='12345'
try:
    istr = int(a)
except:
    istr = -1
print(a)

entr = input('Enter a number')
try:
    val = int(entr)
except:
    val = -1

if val > 0:
    print(val)
else:
    print('not a number')
print('done')



a=max('abcdef')
print(a)
a=min('abcdef')
print(a)
