text = "This is a test!"

def encrypt(text, n):
  for x in range(n):
    even = ''
    odd = ''
    for i in range(len(text)):
      if i%2 != 0:
        even += text[i]
      else:
        odd += text[i]
    text = even + odd

  return text

def decrypt(text, n):
  for x in range(n):
    even = ""
    odd = ""
    
    mid = int(len(text)/2)
    even += text[0:mid]
    odd +=  text[mid:]
    
    textLen = len(text)
    
    text = ""
    
    for i in range(mid):
      text += odd[i] + even[i]
    
    if textLen % 2 != 0:
      text += odd[-1]
    
  return text

new = encrypt(text, 3)

print(decrypt(new, 3))