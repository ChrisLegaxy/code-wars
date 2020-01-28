n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def create_phone_number(n):
  head = ''
  mid = ''
  last = ''

  for i in range(len(n)):
    if i < 3:
      head = head + str(n[i])
    elif i < 6:
      mid = mid + str(n[i])
    elif i < 10:
      last = last + str(n[i])

  return '({}) {}-{}'.format(head, mid, last)

print(create_phone_number(n))
