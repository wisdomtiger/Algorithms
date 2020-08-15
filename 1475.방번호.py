import sys
import math

room = list(str(sys.stdin.readline().rstrip()))
count = 0

matrix = [0 for i in range(10)]

for i in room:
    for j in range(10):
        if(int(i)==j):
            if(j==6 or j==9):
                matrix[6] += 0.5
                matrix[9] += 0.5
            else:
                matrix[j] += 1

print(math.ceil(max(matrix)))