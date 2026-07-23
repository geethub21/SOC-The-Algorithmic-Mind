import sys

input = sys.stdin.readline

MOD = 10**9 + 7

def power(a, b):
    result = 1
    a %= MOD

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % MOD
        a = (a * a) % MOD
        b //= 2

    return result

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print(power(a, b))