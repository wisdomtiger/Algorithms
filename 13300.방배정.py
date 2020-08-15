import sys
import math

n, k = map(int, sys.stdin.readline().split())
matrix = [[0 for i in range(6)] for j in range(2)]
room = 0

for i in range(n):
    s, y = map(int, sys.stdin.readline().split())
    matrix[s][y-1] += 1

for i in range(2):
    for j in range(6):
        if(matrix[i][j]==0):
            continue
        else:
            room += math.ceil(matrix[i][j]/k)

print(room)