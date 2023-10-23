# 05
def ngram(n, seq):
  word = []
  for i in range(len(seq) - n + 1):
    word.append(seq[i:i+n])
  return set(word)
  
a = 'paraparaparadise'
b = 'paragraph'
search = 'se'
x = ngram(2, a)
y = ngram(2, b)
print(f'集合X:{x}')
print(f'集合X:{y}')
print(f'和集合X:{x|y}')
print(f'積集合X:{x&y}')
print(f'差集合X:{x-y}')
print(f'seが集合xに含まれるか:{search in set(x)}')
print(f'seが集合yに含まれるか:{search in set(y)}')