t = int(input())

for _ in range(t):
    y, x = map(int, input().split())
    m = max(x, y)

    if m % 2 == 0:
        if y == m:
            ans = m * m - x + 1
        else:
            ans = (m - 1) * (m - 1) + y
    else:
        if x == m:
            ans = m * m - y + 1
        else:
            ans = (m - 1) * (m - 1) + x

    print(ans)