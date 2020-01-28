n = 456

def digital_root(n):
  strN = str(n)
  if len(strN) > 0:
    sum = 0
    while True:
      if len(str(sum)) >= 0:
        for i in strN:
          sum += int(i)
      else:
        break
  return sum

print(digital_root(n))