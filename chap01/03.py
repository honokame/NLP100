# 03
symbol = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
symbol_list = symbol.replace('.','').split()
symbol_dict = {}

for i, word in enumerate(symbol_list, 1):
  if i in [1,5,6,7,8,9,15,16,19]:
    symbol_dict[word[0]] = i
  else:
    symbol_dict[word[:2]] = i

print(symbol_dict)