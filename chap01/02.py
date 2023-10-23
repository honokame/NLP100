# 02
import re
text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
new_text = text.replace('.', '')
text_cut = re.split('[, ]+',new_text)
ans = [len(i) for i in text_cut]

print(text)
print(new_text)
print(text_cut)
print(ans)