import math

MOD = 10**9 + 7

n, m = map(int, input().split())

ans = 0

for i in range(n):
    ans = (ans + pow(m, math.gcd(i, n), MOD)) % MOD

ans = ans * pow(n, MOD - 2, MOD) % MOD

print(ans)