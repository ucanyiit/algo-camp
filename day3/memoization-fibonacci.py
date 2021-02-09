def fib(N):
    if N <= 1:
        return N
    return fib(N-1) + fib(N-2)
    

def fibMemo(N, memo):
    if N in memo:
        return memo[N]
    if N <= 1:
        return N
    memo[N] = fibMemo(N-1, memo) + fibMemo(N-2, memo)
    return memo[N]

for i in range(20):
    print(fibMemo(i, {}))