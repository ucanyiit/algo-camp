def maxPath(grid, n, m, x, y):
  table = [[] for i in range(n)]
  table[0].append(grid[0][0])
  for i in range(1, m):
    table[0].append(grid[0][i] + table[0][i-1])
  for i in range(1, n):
    table[i].append(grid[i][0] + table[i-1][0])
  
  for i in range(1, n):
    for j in range(1, m):
      new_elem = max(table[i-1][j], table[i][j-1]) + grid[i][j]
      table[i].append(new_elem)

  return table[x][y]
     

grid = [[3, 7, 9, 2, 7], [9, 8, 3, 5, 5], [1, 7, 9, 8, 5], [3, 8, 6, 4, 10], [6, 3, 9, 7, 8]]

print(maxPath(grid, 5, 5, 3, 2))