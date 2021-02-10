N, K = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]

max_bench_count = 0
bench_count = 0

for i in range(0, N):
    removed_index = i-2*K-1
    if(removed_index>=0):
       bench_count -= l[removed_index]
    bench_count+=l[i]
    max_bench_count=max(max_bench_count, bench_count)

print(max_bench_count)