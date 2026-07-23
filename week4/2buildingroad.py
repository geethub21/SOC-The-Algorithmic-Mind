import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parent = list(range(n + 1))
size = [1] * (n + 1)

components = n
largest = 1

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

for _ in range(m):
    a, b = map(int, input().split())

    ra = find(a)
    rb = find(b)

    if ra != rb:
        if size[ra] < size[rb]:
            ra, rb = rb, ra

        parent[rb] = ra
        size[ra] += size[rb]

        components -= 1
        largest = max(largest, size[ra])

    print(components, largest)