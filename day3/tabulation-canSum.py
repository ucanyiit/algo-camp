def canSum(targetSum, numbers):
  table = [True]
  for i in range(1, targetSum+1):
    result = False
    for number in numbers:
      remainder = i-number
      if(remainder < 0):
        continue
      else:
        result = result or table[remainder]
    table.append(result)
  return table[targetSum]
  
print(canSum(7, [2, 3]))
print(canSum(7, [2, 3, 5, 7]))
print(canSum(300, [7, 14]))