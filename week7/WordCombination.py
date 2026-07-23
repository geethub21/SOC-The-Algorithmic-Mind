import sys

input = sys.stdin.readline

MOD = 10**9 + 7

s = input().strip()
n = len(s)

k = int(input())

# Trie
trie = [[-1] * 26]
end = [0]

for _ in range(k):
    word = input().strip()
    node = 0
    for ch in word:
        c = ord(ch) - 97
        if trie[node][c] == -1:
            trie[node][c] = len(trie)
            trie.append([-1] * 26)
            end.append(0)
        node = trie[node][c]
    end[node] += 1

dp = [0] * (n + 1)
dp[n] = 1

for i in range(n - 1, -1, -1):
    node = 0
    j = i
    while j < n:
        c = ord(s[j]) - 97
        nxt = trie[node][c]
        if nxt == -1:
            break
        node = nxt
        if end[node]:
            dp[i] = (dp[i] + dp[j + 1] * end[node]) % MOD
        j += 1

print(dp[0])