n = int(input())
l = [True for x in range(n+1)]

for i in range(2, n+1):
  if(not l[i]):
    continue
  for j in range(2*i, n+1, i):
    l[j] = False

for i in range(1, n+1):
  print(i, l[i])
