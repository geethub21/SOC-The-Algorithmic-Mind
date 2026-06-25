n = int(input())
arr = list(map(int, input().split()))

pos = [0] * (n + 1)

for i, x in enumerate(arr):
    pos[x] = i

rounds = 1

for i in range(1, n):
    if pos[i] > pos[i + 1]:
        rounds += 1

print(rounds)