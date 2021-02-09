def expNaive(n, k):
  result = 1
  for i in range(k):
    result *= n
  return result

def expOptimized(n, k):
  if(k==1):
    return n
  if(k==0):
    return 1
  remainder = n if k%2 else 1
  half = expOptimized(n, k//2)
  return half * half * remainder


n, k = [int(x) for x in input().split()]
expOptimized(n, k)
print("optimized")
expNaive(n, k)
print("naive")