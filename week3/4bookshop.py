import sys

input = sys.stdin.readline

n, x = map(int, input().split())
price = list(map(int, input().split()))
pages = list(map(int, input().split()))

dp = [0] * (x + 1)

for i in range(n):
    p = price[i]
    pg = pages[i]

    for j in range(x, p - 1, -1):
        dp[j] = max(dp[j], dp[j - p] + pg)

print(dp[x])