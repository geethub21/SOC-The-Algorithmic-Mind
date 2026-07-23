from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    dist = [-1] * (n + 1)
    dist[start] = 0

    q = deque([start])

    while q:
        u = q.popleft()

        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)

    farthest = start
    for i in range(1, n + 1):
        if dist[i] > dist[farthest]:
            farthest = i

    return farthest, dist[farthest]

a, _ = bfs(1)
b, diameter = bfs(a)

print(diameter)