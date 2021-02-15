def isPrime(n):
	for i in range(2, int(n**0.5)+1):
		if n%i == 0:
			return False
	return True

fact = []
def factorisation(x):
	i = 2
	while x != 1:
		while x % i == 0:
			x //= i
			fact.append(i)

		if x**0.5 < i:
			fact.append(x)
			break

		i += 1

def multiply(lst):
	result = 1
	for i in lst:
		result *= i
	return result

_ = int(input())
lst = [int(x) for x in input().split()]
output = []
for i in lst:
	factorisation(i)
output = set(fact)

r = multiply(output)
r %= (10**9+7)
print(r)

# Question: https://arsiv.cclub.metu.edu.tr/problem/20brobot/