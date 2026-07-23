import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    heaps = list(map(int, input().split()))

    xor_sum = 0
    for x in heaps:
        xor_sum ^= x

    if xor_sum == 0:
        print("second")
    else:
        print("first")