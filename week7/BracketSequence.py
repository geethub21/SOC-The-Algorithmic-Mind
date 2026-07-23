MOD = 10**9 + 7

n = int(input())

if n % 2 == 1:
    print(0)
    exit()

k = n // 2

fact = [1] * (n + 1)

for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i % MOD

def modinv(x):
    return pow(x, MOD - 2, MOD)

ans = fact[n]
ans = ans * modinv(fact[k]) % MOD
ans = ans * modinv(fact[k]) % MOD
ans = ans * modinv(k + 1) % MOD

print(ans)