import sys

input = sys.stdin.readline

n = int(input())

arrivals = [0] * n
departures = [0] * n

for i in range(n):
    a, b = map(int, input().split())
    arrivals[i] = a
    departures[i] = b

arrivals.sort()
departures.sort()

i = j = 0
current = 0
answer = 0

while i < n:
    if arrivals[i] < departures[j]:
        current += 1
        if current > answer:
            answer = current
        i += 1
    else:
        current -= 1
        j += 1

print(answer)