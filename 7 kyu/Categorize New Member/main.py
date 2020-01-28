data = [[16, 23],[73,1],[56, 20],[1, -1]]

newData = []

for i in data:
    if i[0] >= 55 and i[1] > 7:
        newData.append(str('Senior'))
    else:
        newData.append(str('Open'))

print(newData)
    
    