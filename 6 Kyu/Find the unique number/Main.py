arr = [ 1, 1, 1, 2, 1, 1 ]

def find_uniq(arr):
  count = 0
  count2 = 0
  unique = 0
  unique2 = 0
  for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
      count = count + 1
      unique = arr[i]
    else
      count2 = count2 + 1
  return n

find_uniq(arr)