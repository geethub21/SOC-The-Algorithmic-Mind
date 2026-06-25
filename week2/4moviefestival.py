n = int(input())

movies = []
for _ in range(n):
    a, b = map(int, input().split())
    movies.append((b, a))  # sort by ending time

movies.sort()

count = 0
last_end = 0

for end, start in movies:
    if start >= last_end:
        count += 1
        last_end = end

print(count)