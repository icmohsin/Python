#file = input('Please enter a file :')
file = 'romeo.txt'
try:
    o_file = open(file)
except:
    print('File not found :',file)
    quit()

#f_file = o_file.split()
#print(f_file)
count=0
my_list = list()
for i in o_file:
    s_file = i.strip()
#    s_file = s_file.split(' ')
    #s_file = s_file.strip()
    my_list.append(s_file)

    print('1 : ',s_file)
    #print('2',)
#lst = list()
#for b in my_list:
#    b=b.split(' ')
#    lst.append(b)

my_list.split(' ')
print('3 :',my_list)
