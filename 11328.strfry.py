import sys

n = int(sys.stdin.readline())
for i in range(n):
    a, b = map(str, sys.stdin.readline().split())

    a = sorted(a)
    b = sorted(b)

    if(a==b):
        print("Possible")
    else:
        print("Impossible")