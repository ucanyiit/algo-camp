def isPrimeNaive(n):
  for i in range(2, n):
    if(n%i == 0):
      return False
  return True
  
def isPrimeOptimized(n):
  sqrt_n = int(n**.5+1)
  for i in range(2, sqrt_n):
    if(n%i == 0):
      return False
  return True
  
t = int(input())
a = isPrimeNaive(t)
b = isPrimeOptimized(t)
print(a, b)