# 08
import random
text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
chars, new = "", ""

for word in text.split():
  if len(word) > 4:
    chars = list(word[1:-1])
    random.shuffle(chars)
    new += word[0] + "".join(chars) + word[len(word)-1] + " "
  else:
    new += word + " "

print(text)
print(new)