## 재귀를 쓰면 시간초과가 난다..

import sys

n = int(sys.stdin.readline())

a, b = 0, 1

while n>0:
    a, b = b, a+b
    n -= 1

print(a)