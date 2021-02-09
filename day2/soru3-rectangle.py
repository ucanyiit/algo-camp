N, = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]

stack = [(l[0], 1)]
k = 0

result = 0

for i in range(1, N):
  c = 0
  while(stack and stack[k][0] >= l[i]):
    p = stack.pop()
    c += p[1]
    result = max(p[0] * c, result)
    k -= 1
  stack.append((l[i], c + 1))
  k += 1

c = 0
while(stack):
  p = stack.pop()
  c += p[1]
  result = max(p[0] * c, result)
  k -= 1
  # print((p[0], c), result)

print(result)