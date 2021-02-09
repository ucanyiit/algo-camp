def maxPath(grid, n, m):
  print(n, m)
  if(n==0 and m==0):
    return grid[n][m]
  if(n==0):
    return maxPath(grid, n, m-1) + grid[n][m]
  if(m==0):
    return maxPath(grid, n-1, m) + grid[n][m]
  
  return max(maxPath(grid, n-1, m), maxPath(grid, n, m-1)) + grid[n][m]

def maxPathMemo(grid, n, m, memo):
  if(n==0 and m==0):
    return grid[n][m]
  if((n, m) in memo):
    return memo[(n, m)]
  
  if(n==0):
    memo[(n, m)] = maxPathMemo(grid, n, m-1, memo) + grid[n][m]
  elif(m==0):
    memo[(n, m)] = maxPathMemo(grid, n-1, m, memo) + grid[n][m]
  else:
    memo[(n, m)] = max(maxPathMemo(grid, n-1, m, memo), maxPathMemo(grid, n, m-1, memo)) + grid[n][m]

  return memo[(n, m)]

grid = [[3, 7, 9, 2, 7], [9, 8, 3, 5, 5], [1, 7, 9, 8, 5], [3, 8, 6, 4, 10], [6, 3, 9, 7, 8]]

print(maxPathMemo(grid, 5-1, 5-1, {}))