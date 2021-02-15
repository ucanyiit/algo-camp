for i in range(int(input())):
    n,k=map(int, input().split())
    res=""
    while n>=1:
        res+=str(n%k)
        n=n//k
    print(res[::-1])

# Question: https://arsiv.cclub.metu.edu.tr/problem/basamak/