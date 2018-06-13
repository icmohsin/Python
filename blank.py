import re
txt = '7 and rewarding activity. 568 You can write programs9 for'
val = re.findall('[0-9]+',txt)

print(val)
