temp = []
main = []
high = low = 0

while True:
    temp.append(str(input('Name: ')))
    temp.append(float(input('Weight: ')))
    if len(main) == 0:
        high = low = temp[1]
    else:
        if temp[1] > high:
            hight = temp[1]
        if temp[1] < low:
            low = temp[1]
    main.append(temp[:])
    temp.clear()
    opt = str(input('Do you want to keep?'))
    if opt in 'Nn':
        break
for w in main:
    if p[1] == main:
        print(f'{w[0]}',end='')
