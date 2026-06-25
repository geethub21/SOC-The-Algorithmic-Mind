from bisect import bisect_right, insort
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

movies = []

for _ in range(n):
    a, b = map(int, input().split())
    movies.append((b, a))  # sort by ending time

movies.sort()

available = [0] * k
ans = 0

for end, start in movies:
    pos = bisect_right(available, start)

    if pos == 0:
        continue

    available.pop(pos - 1)
    insort(available, end)
    ans += 1

print(ans)