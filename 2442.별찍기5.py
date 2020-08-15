import sys

star = int(sys.stdin.readline())

for i in range(star):
    print(' '*(star-i-1)+('*'*(2*i+1)))