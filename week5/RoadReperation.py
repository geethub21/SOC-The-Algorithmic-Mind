import sys

input = sys.stdin.readline

n, m = map(int, input().split())

edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

parent = list(range(n + 1))
size = [1] * (n + 1)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # Path compression
        x = parent[x]
    return x

def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra == rb:
        return False

    if size[ra] < size[rb]:
        ra, rb = rb, ra

    parent[rb] = ra
    size[ra] += size[rb]
    return True

cost = 0
edges_used = 0

for c, a, b in edges:
    if union(a, b):
        cost += c
        edges_used += 1

if edges_used == n - 1:
    print(cost)
else:
    print("IMPOSSIBLE")