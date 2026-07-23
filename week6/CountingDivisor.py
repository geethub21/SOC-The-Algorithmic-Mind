import sys

input = sys.stdin.readline

MAX = 10**6

divisors = [0] * (MAX + 1)

# Precompute divisor counts
for i in range(1, MAX + 1):
    for j in range(i, MAX + 1, i):
        divisors[j] += 1

n = int(input())

for _ in range(n):
    x = int(input())
    print(divisors[x])