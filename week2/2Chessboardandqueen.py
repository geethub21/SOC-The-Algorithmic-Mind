board = [input().strip() for _ in range(8)]

cols = [False] * 8
diag1 = [False] * 15  # row + col
diag2 = [False] * 15  # row - col + 7

ans = 0

def backtrack(row):
    global ans

    if row == 8:
        ans += 1
        return

    for col in range(8):
        if board[row][col] == '*':
            continue

        d1 = row + col
        d2 = row - col + 7

        if cols[col] or diag1[d1] or diag2[d2]:
            continue

        cols[col] = diag1[d1] = diag2[d2] = True
        backtrack(row + 1)
        cols[col] = diag1[d1] = diag2[d2] = False

backtrack(0)
print(ans)