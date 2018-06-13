a=input('Please enter the Score : ')
try:
    a=float(a)
except:
    a=-1

if a>1.0 or a < 0.0:
    print ('Bad Score')
elif a >= 0.9:
    print ('A')
elif a >=0.8:
    print ('B')
elif a >= 0.7:
    print ('C')
elif a >=0.6:
    print ('C')
elif a <0.6:
    print ('F')
