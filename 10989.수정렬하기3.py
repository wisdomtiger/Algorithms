import sys

n = int(sys.stdin.readline())

arr = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    arr[data] += 1

for i in range(10001):
    while arr[i] != 0:
        print(i)
        arr[i] -= 1