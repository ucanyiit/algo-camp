def bestSum(targetSum, numbers):
  table = [0]

  for i in range(1, targetSum+1):
    l = []
    for number in numbers:
      remainder = i - number
      if remainder < 0 or table[remainder] is False:
        continue
      l.append(table[remainder])
    if(l):
      table.append(min(l)+1)
    else:
      table.append(False)
  # print(table)
  return table[targetSum]
  
print(bestSum(7, [2, 3]))
print(bestSum(7, [2, 3, 5, 7]))
print(bestSum(300, [7, 14]))