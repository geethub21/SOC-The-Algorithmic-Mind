import sys

sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

state = [0] * (n + 1)
parent = [-1] * (n + 1)

cycle = []


def dfs(v):
    global cycle

    state[v] = 1

    for u in graph[v]:
        if state[u] == 0:
            parent[u] = v
            if dfs(u):
                return True

        elif state[u] == 1:
            cycle = [u]
            cur = v

            while cur != u:
                cycle.append(cur)
                cur = parent[cur]

            cycle.append(u)
            cycle.reverse()

            return True

    state[v] = 2
    return False


for i in range(1, n + 1):
    if state[i] == 0:
        if dfs(i):
            print(len(cycle))
            print(*cycle)
            sys.exit()

print("IMPOSSIBLE")