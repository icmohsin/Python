#exeercise for chap 5
num = 0
tot = 0.0

while True:
    inp= input('Please enter a number : ')

    if inp == 'done':
        break
    else:
        try:
            inpu = float(inp)
            num = num+1
            tot = tot+inpu
        except:
            print('Invalid Input')

print(round(tot),num,tot/num)
