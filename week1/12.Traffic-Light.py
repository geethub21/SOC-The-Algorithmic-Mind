x, n = map(int, input().split())
p = list(map(int, input().split()))

pos = [0] + sorted(p) + [x]

left = {}
right = {}

for i in range(len(pos)):
    if i > 0:
        left[pos[i]] = pos[i - 1]
    if i < len(pos) - 1:
        right[pos[i]] = pos[i + 1]

cur_max = 0
for i in range(1, len(pos)):
    cur_max = max(cur_max, pos[i] - pos[i - 1])

ans = [cur_max]

for light in reversed(p):
    l = left[light]
    r = right[light]

    cur_max = max(cur_max, r - l)

    right[l] = r
    left[r] = l

    ans.append(cur_max)

print(*ans[-2::-1])