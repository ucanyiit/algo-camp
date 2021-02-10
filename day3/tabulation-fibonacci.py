def fib(N):
    table = [0, 1]
    for i in range(2, N+1):
      new_elem = table[i-1] + table[i-2]
      table.append(new_elem)
    return table[N]

print(fib(50))