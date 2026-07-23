import sys

input = sys.stdin.readline

MOD = 10**9 + 7

n = int(input())
pat = input().strip()

m = len(pat)

# KMP prefix function
lps = [0] * m
j = 0
for i in range(1, m):
    while j > 0 and pat[i] != pat[j]:
        j = lps[j - 1]
    if pat[i] == pat[j]:
        j += 1
        lps[i] = j

# automaton[state][char]
aut = [[0] * 26 for _ in range(m + 1)]

for state in range(m + 1):
    for c in range(26):
        if state == m:
            aut[state][c] = m
            continue

        k = state
        ch = chr(ord('A') + c)

        while k > 0 and pat[k] != ch:
            k = lps[k - 1]

        if pat[k] == ch:
            k += 1

        aut[state][c] = k

dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(n):
    for state in range(m + 1):
        if dp[i][state] == 0:
            continue

        for c in range(26):
            nxt = aut[state][c]
            dp[i + 1][nxt] = (dp[i + 1][nxt] + dp[i][state]) % MOD

print(dp[n][m])