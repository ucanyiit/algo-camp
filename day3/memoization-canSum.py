def canSum(targetSum, numbers):
  if(targetSum < 0):
    return False
  if(targetSum == 0):
    return True
  
  for number in numbers:
    remainder = targetSum - number
    if canSum(remainder, numbers):
      return True 
  
  return False

def canSumMemo(targetSum, numbers, memo):
  if(targetSum in memo):
    return memo[targetSum]
  if(targetSum < 0):
    return False
  if(targetSum == 0):
    return True
  
  for number in numbers:
    remainder = targetSum - number
    if canSumMemo(remainder, numbers, memo):
      memo[targetSum] = True
      return True 

  memo[targetSum] = False
  return False
  
print(canSumMemo(7, [2, 3], {}))
print(canSumMemo(7, [2, 3, 5, 7], {}))
print(canSumMemo(300, [7, 14], {}))