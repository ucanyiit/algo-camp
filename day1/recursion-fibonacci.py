# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.fib(N-1) + self.fib(N-2)

instance = Solution()
result = instance.fib(12)
print(result)