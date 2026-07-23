import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n + 1)
depth = [0] * (n + 1)
order = []

# Iterative DFS
stack = [1]
while stack:
    v = stack.pop()
    order.append(v)
    for u in graph[v]:
        if u != parent[v]:
            parent[u] = v
            depth[u] = depth[v] + 1
            stack.append(u)

sub = [1] * (n + 1)

# Compute subtree sizes
for v in reversed(order):
    if parent[v]:
        sub[parent[v]] += sub[v]

ans = [0] * (n + 1)
ans[1] = sum(depth)

# Reroot DP
for v in order:
    for u in graph[v]:
        if u != parent[v]:
            ans[u] = ans[v] + n - 2 * sub[u]

print(*ans[1:])