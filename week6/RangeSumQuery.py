n, q = map(int, input().split())

arr = list(map(int, input().split()))

# Build prefix sum array
prefix = [0] * (n + 1)

for i in range(n):
    prefix[i + 1] = prefix[i] + arr[i]

# Answer queries
for _ in range(q):
    a, b = map(int, input().split())
    print(prefix[b] - prefix[a - 1])