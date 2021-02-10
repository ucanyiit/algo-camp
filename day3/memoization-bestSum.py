def bestSum(targetSum, numbers, memo):
  if(targetSum in memo):
    return memo[targetSum]
  if(targetSum < 0):
    return False
  if(targetSum == 0):
    return 0
  
  result = False

  l = []

  for number in numbers:
    remainder = targetSum - number
    remainderSum = bestSum(remainder, numbers, memo)
    if remainderSum is not False:
      l.append(remainderSum)

  if(l):
    result = min(l) + 1
  
  memo[targetSum] = result

  return result

def bestSumMemo(targetSum, numbers, memo):
  if(targetSum in memo):
    return memo[targetSum]
  if(targetSum < 0):
    return False
  if(targetSum == 0):
    return 0
  
  result = False

  for number in numbers:
    remainder = targetSum - number
    remainderSum = bestSumMemo(remainder, numbers, memo)
    if remainderSum is not False:
      if result is False:
        result = remainderSum + 1
      else:
        result = min(result, remainderSum + 1)
  
  memo[targetSum] = result
  return result
  
print(bestSum(7, [2, 3], {}))
print(bestSum(7, [2, 3, 5, 7], {}))
print(bestSum(300, [7, 14], {}))