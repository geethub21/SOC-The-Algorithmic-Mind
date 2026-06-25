n, x = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
curr_sum = 0
count = 0

for right in range(n):
    curr_sum += arr[right]

    while curr_sum > x:
        curr_sum -= arr[left]
        left += 1

    if curr_sum == x:
        count += 1

print(count)