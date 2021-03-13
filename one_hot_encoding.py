def word_to_one_hot(word):
  lis=[]
  for i in V['Values']:
    if i.strip() in word.strip() and word.strip() in i.strip():
      lis.append(1)
    else:
      lis.append(0)
  return lis