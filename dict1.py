import string

file=input('Please enter file name :')
words = dict()

try  :
    o_file=open(file)
except:
    print('file not found')
    exit()

for i in o_file:
    #print('i : ',i)
    wds = i.strip()
    #print('wds : ',wds)
    #removing punctuation and replacing spaces
    wds = wds.translate(wds.maketrans('','',string.punctuation))
    #lower all values
    wds = wds.lower()
    #print(wds)
    wds = wds.split()
    for x in wds:
        words[x] = words.get(x,0)+1
        #if x not in words:
        #    words[x]=1
        #else:
        #    words[x] = words[x]+1

print(words)

for val,st in words.items():
    print (val,' :: ',st)
#for ss in words:
    #print(ss, words[ss])

#print(words)
