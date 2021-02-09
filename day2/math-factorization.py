N = int(input())

k = N**(1/2)

l = [1, N]

for i in range(2, int(k)+1):
  if(N%i == 0):
    l.append(i)
    if(N / i != i):
      l.append(N//i)
  
l = sorted(l)

print(l)