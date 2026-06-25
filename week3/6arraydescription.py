import sys

MOD = 1000000007

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

prev = [0] * (m + 2)

if arr[0] == 0:
    for v in range(1, m + 1):
        prev[v] = 1
else:
    prev[arr[0]] = 1

for i in range(1, n):
    curr = [0] * (m + 2)

    if arr[i] == 0:
        for v in range(1, m + 1):
            curr[v] = (
                prev[v - 1]
                + prev[v]
                + prev[v + 1]
            ) % MOD
    else:
        v = arr[i]
        curr[v] = (
            prev[v - 1]
            + prev[v]
            + prev[v + 1]
        ) % MOD

    prev = curr

print(sum(prev) % MOD)