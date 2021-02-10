def fib(N):
    if N <= 1:
        return N
    return fib(N-1) + fib(N-2)

def fibMemo(N, memo):
    if memo[N] is not False:
        return memo[N]
    if N <= 1:
        return N
    memo[N] = fibMemo(N-1, memo) + fibMemo(N-2, memo)
    return memo[N]

print(fibMemo(50, [False] * 60))
print(fib(50))
