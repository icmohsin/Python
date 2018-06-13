import re


s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)



hand = open('new.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-z0-9]\S+@\S+[a-zA-z0-9]', line)
    if len(x) > 0:
        print(x)
    if re.search('^X\S*:',line):
        print (line)


val = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
ex = re.findall('\S+@\S+',val)
print(ex)


x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
