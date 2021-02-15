n, k = [int(x) for x in input().split()]

def obsession(n, k, memo):
	if (n, k) in memo:
		return memo[(n, k)]

	if n == 1 and 0<=k<=9:
		memo[(n, k)] = 1
		return 1
	elif n == 1 and k<0:
		memo[(n, k)] = 0
		return 0
	elif n == 1 and k>9:
		memo[(n, k)] = 0
		return 0

	result = 0
	for i in range(10):
		result += obsession(n-1, k-i, memo)
		
	memo[(n, k)] = result
	return result

a = obsession(n, k, {})
a %= 10**9+7
print(a)