def howSum(targetSum, numbers):
  if(targetSum < 0):
    return False
  if(targetSum == 0):
    return []

  for number in numbers:
    remainder = targetSum - number
    result = howSum(remainder, numbers)
    if(result is not False):
      result.append(number)
      break
  
  return result

def howSumMemo(targetSum, numbers, memo):
  if(targetSum in memo):
    return memo[targetSum]
  if(targetSum < 0):
    return False
  if(targetSum == 0):
    return []

  for number in numbers:
    remainder = targetSum - number
    result = howSumMemo(remainder, numbers, memo)
    if(result is False):
      continue
    else:
      result.append(number)
      break
  
  memo[targetSum] = result

  return result
  
print(howSumMemo(7, [2, 3], {}))
print(howSumMemo(7, [2, 3, 5, 7], {}))
print(howSumMemo(300, [7, 14], {}))