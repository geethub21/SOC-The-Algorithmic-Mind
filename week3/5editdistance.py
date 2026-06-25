import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

n = len(a)
m = len(b)

prev = list(range(m + 1))

for i in range(1, n + 1):
    curr = [i] + [0] * m

    for j in range(1, m + 1):
        if a[i - 1] == b[j - 1]:
            curr[j] = prev[j - 1]
        else:
            curr[j] = 1 + min(
                prev[j],      # delete
                curr[j - 1],  # insert
                prev[j - 1]   # replace
            )

    prev = curr

print(prev[m])