n = 153

def narcissistic(value):
  valueLen = len(str(value))
  eachValue = [int(i) for i in str(value)]
  sumOfEachValue = 0

  for i in eachValue:
    sumOfEachValue += i ** valueLen
  
  if value == sumOfEachValue:
    return True
  else:
    return False


print(narcissistic(n))