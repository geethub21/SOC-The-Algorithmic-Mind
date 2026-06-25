n = int(input())
sticks = list(map(int, input().split()))

sticks.sort()
median = sticks[n // 2]

cost = sum(abs(x - median) for x in sticks)
print(cost)