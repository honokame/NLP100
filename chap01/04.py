# 04
def ngram(n, seq):
  word = []
  for i in range(len(seq) - n + 1):
    word.append(seq[i:i+n])
  print(word)
  
seq = 'I am an NLPer'
for i in range(1, 4):
  ngram(i, seq.split())
  ngram(i, list(seq))