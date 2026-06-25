import sys

MOD = 1000000007

input = sys.stdin.readline

t = int(input())

queries = [int(input()) for _ in range(t)]
mx = max(queries)

dp1 = [0] * (mx + 1)
dp2 = [0] * (mx + 1)

dp1[1] = 1
dp2[1] = 1

for i in range(2, mx + 1):
    dp1[i] = (4 * dp1[i - 1] + dp2[i - 1]) % MOD
    dp2[i] = (dp1[i - 1] + 2 * dp2[i - 1]) % MOD

for n in queries:
    print((dp1[n] + dp2[n]) % MOD)