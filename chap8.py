friends = ['a','b','c']
print (friends)
for i in friends:
    print(i)
friends[1]='done'
friends.append('append')
print(friends)
print(range(len(friends)))
if 'a' in friends:
    print('yes')
if 'dd' not in friends:
    print('no')
friends.sort()
print('Sort is Ö ',friends)

a='Hi; this; is;  my new list'
a=a.split(';')
print(a)

friends = [ 'Joseph', 'Glenn', 'Sally' ]
print(friends[2:1])

t = [9, 41, 12, 3, 74, 15]
print(t[2:4])
