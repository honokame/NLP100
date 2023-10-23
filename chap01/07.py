# 07
def cipher(text):
  generate = ''
  for char in text:
    if char.islower():
      generate += chr(219 - ord(char))
    else :
      generate += char
  return(generate)

text = 'this is a message.'
print(cipher(text))
print(cipher(cipher(text)))