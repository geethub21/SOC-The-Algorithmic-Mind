n, m, k = map(int, input().split())

applicants = list(map(int, input().split()))
apartments = list(map(int, input().split()))

applicants.sort()
apartments.sort()

i = j = 0
ans = 0

while i < n and j < m:
    if apartments[j] < applicants[i] - k:
        j += 1
    elif apartments[j] > applicants[i] + k:
        i += 1
    else:
        ans += 1
        i += 1
        j += 1

print(ans)