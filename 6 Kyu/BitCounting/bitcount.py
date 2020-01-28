n = int(10)
binaryString = ''

while n!=0:
    binaryNumber = n%2
    n = n/2
    n = int(n)
    binaryString += str(binaryNumber)

binaryString = binaryString[::-1]

#Count Number of 1

for i in binaryString:
    if i == '1':
        count += 1

print(count)

print(binaryString)
