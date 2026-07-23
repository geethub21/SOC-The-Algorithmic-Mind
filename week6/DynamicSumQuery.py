import sys

input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))

bit = [0] * (n + 1)

def update(i, delta):
    while i <= n:
        bit[i] += delta
        i += i & -i

def query(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

# Build the Fenwick Tree
for i in range(n):
    update(i + 1, arr[i])

for _ in range(q):
    t, a, b = map(int, input().split())

    if t == 1:
        delta = b - arr[a - 1]
        arr[a - 1] = b
        update(a, delta)
    else:
        print(query(b) - query(a - 1))