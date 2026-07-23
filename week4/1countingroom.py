from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

rooms = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            rooms += 1

            q = deque([(i, j)])
            grid[i][j] = '#'

            while q:
                x, y = q.popleft()

                if x > 0 and grid[x - 1][y] == '.':
                    grid[x - 1][y] = '#'
                    q.append((x - 1, y))

                if x < n - 1 and grid[x + 1][y] == '.':
                    grid[x + 1][y] = '#'
                    q.append((x + 1, y))

                if y > 0 and grid[x][y - 1] == '.':
                    grid[x][y - 1] = '#'
                    q.append((x, y - 1))

                if y < m - 1 and grid[x][y + 1] == '.':
                    grid[x][y + 1] = '#'
                    q.append((x, y + 1))

print(rooms)