n = int(input())

position = []

for i in range(n):
    x, y = list(map(int,input().split()))
    position.append([x,y])

position = sorted(position,key=lambda x : (x[0], x[1]))

for i in position:
    print(i[0],i[1])