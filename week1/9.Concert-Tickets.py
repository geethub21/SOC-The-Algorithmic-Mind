import sys
from bisect import bisect_right

input = sys.stdin.readline

n, m = map(int, input().split())
tickets = list(map(int, input().split()))
customers = list(map(int, input().split()))

tickets.sort()

parent = list(range(n + 1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

for x in customers:
    pos = bisect_right(tickets, x)

    pos = find(pos)

    if pos == 0:
        print(-1)
    else:
        print(tickets[pos - 1])
        parent[pos] = find(pos - 1)