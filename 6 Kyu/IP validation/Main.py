ip = '123.45.67.89'
import re

# PAUSE

def is_valid_IP(strng):
  ipSplit = strng.split('.')

  if len(ipSplit) != 4:
    return False
  for i in ipSplit:
    checkAlpha = re.search('[a-zA-Z]', i)
    if checkAlpha:
      return False
    if i[0] == 0:
      return False
  return True

is_valid_IP(ip)