iterable = 'AAAABBBCCDAABBB'
newArray = []
position = 0

for element in iterable:
  if len(newArray) < 1:
    newArray.append(element)
    pass
  if newArray[len(newArray) - 1] != element:
    newArray.append(element)
  


print(iterable)
print(newArray)