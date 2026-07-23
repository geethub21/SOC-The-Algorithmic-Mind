import sys

input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))

size = 1
while size < n:
    size *= 2

tree = [float('inf')] * (2 * size)

# Build the leaves
for i in range(n):
    tree[size + i] = arr[i]

# Build the internal nodes
for i in range(size - 1, 0, -1):
    tree[i] = min(tree[2 * i], tree[2 * i + 1])

# Answer queries
for _ in range(q):
    l, r = map(int, input().split())
    l = l - 1 + size
    r = r - 1 + size

    ans = float('inf')

    while l <= r:
        if l % 2 == 1:
            ans = min(ans, tree[l])
            l += 1
        if r % 2 == 0:
            ans = min(ans, tree[r])
            r -= 1
        l //= 2
        r //= 2

    print(ans)