import random

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)


cap_letter1 = chr(random.randint(65,90))
cap_letter2 = chr(random.randint(65,90))
cap_letter3 = chr(random.randint(65,90))

lower_letter1 = chr(random.randint(97,122))
lower_letter2 = chr(random.randint(97,122))
lower_letter3 = chr(random.randint(97,122))

digit1 = chr(random.randint(48,57))
digit2 = chr(random.randint(48,57))
digit3 = chr(random.randint(48,57))

print(cap_letter1, cap_letter2, cap_letter3, lower_letter1, lower_letter2, lower_letter3, digit1, digit2, digit3)

password = list(cap_letter1 + cap_letter2 + cap_letter3 + lower_letter1 + lower_letter2 + lower_letter3 + digit1 + digit2 + digit3)

print(password)
password = shuffle(password)
print(password)

