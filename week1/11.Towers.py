from bisect import bisect_right

n = int(input())
cubes = list(map(int, input().split()))

tops = []

for x in cubes:
    pos = bisect_right(tops, x)

    if pos == len(tops):
        tops.append(x)
    else:
        tops[pos] = x

print(len(tops))