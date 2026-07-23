from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# Topological Sort
q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

topo = []

while q:
    node = q.popleft()
    topo.append(node)

    for nei in graph[node]:
        indegree[nei] -= 1
        if indegree[nei] == 0:
            q.append(nei)

# DP
NEG = -10**18
dp = [NEG] * (n + 1)
parent = [-1] * (n + 1)

dp[1] = 1

for node in topo:
    if dp[node] == NEG:
        continue

    for nei in graph[node]:
        if dp[node] + 1 > dp[nei]:
            dp[nei] = dp[node] + 1
            parent[nei] = node

if dp[n] == NEG:
    print("IMPOSSIBLE")
    sys.exit()

# Reconstruct Path
path = []
cur = n

while cur != -1:
    path.append(cur)
    cur = parent[cur]

path.reverse()

print(len(path))
print(*path)