class Solution:
  def encrypt(t, k, d, d2):
    output = str()
    for i in range(len(t)):
      if ((t[i]<'a' or t[i]>'z') and (t[i]<'A' or t[i]>'Z')):
        output+=t[i]
        continue
      if t[i] in d.keys():
        f = (d[t[i]] + d[k[i]]) % 26
        output+=d2[f]
      else:
        f = (d[t[i].lower()] + d[k[i]]) % 26
        output+=d2[f].upper()
    return output

  def decrypt(t, k, d, d2, ind):
    output = str()
    for i in range(len(t)):
      if i in ind:
        output+=" "
      if ((t[i]<'a' or t[i]>'z') and (t[i]<'A' or t[i]>'Z')):
        output+=t[i]
        continue
      if t[i] in d.keys():
        f = (d[t[i]] - d[k[i]] + 26) % 26
        output+=d2[f]
      else:
        f = (d[t[i].lower()] - d[k[i]] + 26) % 26
        output+=d2[f].upper()
    return output

  d = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5,'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
  d2 = dict(map(reversed, d.items()))
  text = input()
  key = input()
  some = str()
  q = 0
  w = 0
  indexes = []
  for i in range(len(text)):
    if text[i]==' ':
      indexes.append(i-w)
      w+=1
      continue
    elif ((text[i]<'a' or text[i]>'z') and (text[i]<'A' or text[i]>'Z')):
      some+=text[i]
      continue
    if q==len(key):
      q = 0
    some+=key[q]
    q+=1
  sol = encrypt(text.replace(" ", ""), some.lower(), d, d2)
  print(sol)
  print(decrypt(sol, some.lower(), d, d2, indexes))