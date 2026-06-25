n, x = map(int, input().split())
coins = list(map(int, input().split()))

INF = x + 1
dp = [INF] * (x + 1)
dp[0] = 0

for coin in coins:
    for s in range(coin, x + 1):
        dp[s] = min(dp[s], dp[s - coin] + 1)

print(dp[x] if dp[x] != INF else -1)