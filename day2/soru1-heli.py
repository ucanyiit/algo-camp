N, M = [int(x) for x in input().split()]

# N, M = [1, 2]

count = 0

for i in range(0, N):
    X, Y, Z = [int(x) for x in input().split()]
    l=(X**2 + Y**2 + Z**2)**(1/2)
    if l * 2 <= M:
        count += 1

print(count)