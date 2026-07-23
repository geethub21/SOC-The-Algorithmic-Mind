import sys

input = sys.stdin.readline

text = input().strip()
pattern = input().strip()

m = len(pattern)

# Build LPS array
lps = [0] * m
j = 0

for i in range(1, m):
    while j > 0 and pattern[i] != pattern[j]:
        j = lps[j - 1]
    if pattern[i] == pattern[j]:
        j += 1
        lps[i] = j

# KMP Search
count = 0
j = 0

for ch in text:
    while j > 0 and ch != pattern[j]:
        j = lps[j - 1]
    if ch == pattern[j]:
        j += 1
    if j == m:
        count += 1
        j = lps[j - 1]

print(count)