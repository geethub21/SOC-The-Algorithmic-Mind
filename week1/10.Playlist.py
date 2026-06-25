n = int(input())
songs = list(map(int, input().split()))

seen = set()
left = 0
ans = 0

for right in range(n):
    while songs[right] in seen:
        seen.remove(songs[left])
        left += 1

    seen.add(songs[right])
    ans = max(ans, right - left + 1)

print(ans)