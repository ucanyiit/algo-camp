def howSum(targetSum, numbers):
  table = [[]]
  for i in range(1, targetSum+1):
    result = False
    for number in numbers:
      remainder = i-number
      if(remainder < 0):
        continue
      if(table[remainder] is False):
        continue
      result = table[remainder].copy()
      result.append(number)
      break
    table.append(result)

  return table[targetSum]
  
  
print(howSum(7, [2, 3]))
print(howSum(7, [2, 3, 5, 7]))
print(howSum(300, [7, 14]))