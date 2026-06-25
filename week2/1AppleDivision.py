def appleDivision(n, arr):
    total = sum(arr)
    ans = float('inf')

    def dfs(i, curr_sum):
        nonlocal ans

        if i == n:
            ans = min(ans, abs(total - 2 * curr_sum))
            return

        dfs(i + 1, curr_sum + arr[i])  # include arr[i]
        dfs(i + 1, curr_sum)           # exclude arr[i]

    dfs(0, 0)
    return ans


n = int(input())
arr = list(map(int, input().split()))

print(appleDivision(n, arr))