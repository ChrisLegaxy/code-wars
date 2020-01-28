word = 'abc'


newWords = [word[i:i+2] for i in range(0, len(word), 2)]
newWordss = []

print(newWords)

for i in newWords:
  if len(i) < 2:
    i += '_'
  newWordss.append(i)
  

print(newWords)
print(newWordss)