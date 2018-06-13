dct = dict()
dct['first'] = 'Hallo '

dct = {'second':'How ','third':'are you !'}
#print (dct)

count=dict()
new_count=dict()
names = ['Monu','Sonu','Monu','Aaban','Monu','Sonu','Aaira']
#print(names)
for name in names:
    #print('lp start : ',name)
    if name not in count:
        count[name] = 1
    else:
        count[name] = count[name] + 1
        #print('else ',count)
print(count)

#get gets the value from list if not assign zero and then add one to ita
for name in names:
    new_count[name] = new_count.get(name,0) +1
print('new count is : ',new_count)
