import sys

n, x = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

a = [(arr[i], i + 1) for i in range(n)]
a.sort()

l, r = 0, n - 1

while l < r:
    s = a[l][0] + a[r][0]

    if s == x:
        print(a[l][1], a[r][1])
        break
    elif s < x:
        l += 1
    else:
        r -= 1
else:
    print("IMPOSSIBLE")