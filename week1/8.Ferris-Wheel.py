n, x = map(int, input().split())
w = list(map(int, input().split()))

w.sort()

i = 0
j = n - 1
gondolas = 0

while i <= j:
    if w[i] + w[j] <= x:
        i += 1
        j -= 1
    else:
        j -= 1

    gondolas += 1

print(gondolas)