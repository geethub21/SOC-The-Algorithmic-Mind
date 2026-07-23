from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

color = [0] * (n + 1)   # 0 = unvisited, 1 and 2 are the two teams

for start in range(1, n + 1):
    if color[start] != 0:
        continue

    color[start] = 1
    q = deque([start])

    while q:
        node = q.popleft()

        for nei in graph[node]:
            if color[nei] == 0:
                color[nei] = 3 - color[node]   # Switch between 1 and 2
                q.append(nei)
            elif color[nei] == color[node]:
                print("IMPOSSIBLE")
                sys.exit()

print(*color[1:])